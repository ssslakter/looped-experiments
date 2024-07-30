# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_models.ipynb.

# %% auto 0
__all__ = ['MaskedTransformer', 'Transformer', 'LoopedTransformer']

# %% ../nbs/02_models.ipynb 4
import math

import torch
import torch.nn.functional as F
from torch import nn

from .nano_gpt import Block, LayerNorm

# %% ../nbs/02_models.ipynb 5
class MaskedTransformer(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        self.freq = 2 # one input, one output, and so on
        self.block_size = cfg.n_positions * self.freq + 1  # input, output pairs + 1 for the target
        self.transformer = nn.ModuleDict(dict(
            wpe=nn.Embedding(self.block_size, cfg.n_embd),
            drop=nn.Dropout(cfg.dropout),
            h=nn.ModuleList([Block(cfg) for _ in range(cfg.n_layer)]),
            ln_f=LayerNorm(cfg.n_embd, bias=cfg.bias),
        ))
        if self.__class__ == MaskedTransformer:
            self._init_all_params(cfg.n_layer)

    def _init_weights(self, module):
        if isinstance(module, nn.Linear):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)
            if module.bias is not None:
                torch.nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)

    def _init_all_params(self):
        # init all weights
        self.apply(self._init_weights)
        # apply special scaled init to the residual projections, per GPT-2 paper
        for pn, p in self.named_parameters():
            if pn.endswith('c_proj.weight'):
                torch.nn.init.normal_(p, mean=0.0, std=0.02 / math.sqrt(2 * self.cfg.n_layer))

    def forward(self, embs):
        device = embs.device
        bs, t, dim = embs.size()
        assert t <= self.block_size, f"Cannot forward sequence of length {t}, block size is only {self.block_size}"
        pos = torch.arange(0, t, dtype=torch.long, device=device)

        pos_emb = self.transformer.wpe(pos)
        x = self.transformer.drop(embs + pos_emb)
        for block in self.transformer.h:
            x = block(x+embs)
        x = self.transformer.ln_f(x)

        return x

# %% ../nbs/02_models.ipynb 6
class Transformer(MaskedTransformer):
    '''Transformer for tasks from in-context learning'''

    def __init__(self, cfg):
        super().__init__(cfg)
        self.read_in = nn.Linear(cfg.n_dims, cfg.n_embd)
        self.read_out = nn.Linear(cfg.n_embd, 1)

        self._init_all_params()

    def create_prompt(self, xs, ys):
        n_dims = xs.shape[-1]
        y_wide = F.pad(ys.unsqueeze(-1), (0, n_dims - 1), value=0)
        return torch.stack((xs, y_wide), dim=2).flatten(1, 2)

    def forward(self, xs, ys):
        x = self.create_prompt(xs, ys)
        x = self.read_in(x)
        x = super().forward(x)
        y = self.read_out(x).squeeze(-1)
        y = y[:, ::self.freq] # only take the outputs (every other element)
        return y

# %% ../nbs/02_models.ipynb 7
class LoopedTransformer(MaskedTransformer):
    '''Looped transformer for tasks from in-context learning'''

    def __init__(self, cfg):
        super().__init__(cfg)
        self.read_in = nn.Linear(cfg.n_dims, cfg.n_embd)
        self.read_out = nn.Linear(cfg.n_embd, 1)

        self._init_all_params()

    def create_prompt(self, xs, ys):
        n_dims = xs.shape[-1]
        y_wide = F.pad(ys.unsqueeze(-1), (0, n_dims - 1), value=0)
        return torch.stack((xs, y_wide), dim=2).flatten(1, 2)

    def forward(self, xs, ys):
        x = self.create_prompt(xs, ys)
        x = self.read_in(x)
        x = super().forward(x)
        y = self.read_out(x).squeeze(-1)
        y = y[:, ::self.freq] # only take the outputs (every other element)
        return y
