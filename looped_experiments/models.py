# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_models.ipynb.

# %% auto 0
__all__ = ['MaskedTransformer', 'init_weights', 'init_all_params', 'Transformer', 'LoopedTransformer', 'loop_loss', 'get_model',
           'get_loss']

# %% ../nbs/02_models.ipynb 1
import math

import torch
import torch.nn.functional as F
from torch import nn

from .nano_gpt import Block, LayerNorm
from .utils import get_config, show_config

# %% ../nbs/02_models.ipynb 2
class MaskedTransformer(nn.Module):
    def __init__(self, cfg, freq=2):
        super().__init__()
        self.cfg = cfg
        self.block_size = cfg.n_positions * freq + 1  # input, output pairs + 1 for the target
        self.transformer = nn.ModuleDict(dict(
            wpe=nn.Embedding(self.block_size, cfg.n_embd),
            drop=nn.Dropout(cfg.dropout),
            h=nn.ModuleList([Block(cfg) for _ in range(cfg.n_layer)]),
            ln_f=LayerNorm(cfg.n_embd, bias=cfg.bias),
        ))
        if self.__class__ == MaskedTransformer: init_all_params(self)

    def forward(self, embs):
        device = embs.device
        bs, t, dim = embs.size()
        assert t <= self.block_size, f"Cannot forward sequence of length {t}, block size is only {self.block_size}"
        pos = torch.arange(0, t, dtype=torch.long, device=device)

        pos_emb = self.transformer.wpe(pos)
        x = self.transformer.drop(embs + pos_emb)
        for block in self.transformer.h:
            x = block(x)
        x = self.transformer.ln_f(x)

        return x
    
def init_weights(module):
    if isinstance(module, nn.Linear):
        torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)
        if module.bias is not None: torch.nn.init.zeros_(module.bias)
    elif isinstance(module, nn.Embedding):
        torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)

def init_all_params(model):
    # init all weights
    model.apply(init_weights)
    # apply special scaled init to the residual projections, per GPT-2 paper
    for pn, p in model.named_parameters():
        if pn.endswith('c_proj.weight'):
            torch.nn.init.normal_(p, mean=0.0, std=0.02 / math.sqrt(2 * model.cfg.n_layer))

# %% ../nbs/02_models.ipynb 3
class Transformer(nn.Module):
    '''Transformer for tasks from in-context learning'''

    def __init__(self, cfg, freq=2):
        super().__init__()
        self.cfg = cfg
        self.freq = freq  # one input, one output, and so on
        self.backbone = MaskedTransformer(cfg, freq)
        self.read_in = nn.Linear(cfg.n_dims, cfg.n_embd)
        self.read_out = nn.Linear(cfg.n_embd, 1)

        init_all_params(self)

    def create_prompt(self, xs, ys):
        n_dims = xs.shape[-1]
        y_wide = F.pad(ys.unsqueeze(-1), (0, n_dims - 1), value=0)
        return torch.stack((xs, y_wide), dim=2).flatten(1, 2)

    def forward(self, xs, ys):
        x = self.create_prompt(xs, ys)
        x = self.read_in(x)
        x = self.backbone(x)
        y = self.read_out(x).squeeze(-1)
        y = y[:, ::self.freq]  # only take the outputs (every other element)
        return y

# %% ../nbs/02_models.ipynb 4
class LoopedTransformer(Transformer):
    '''Looped transformer for tasks from in-context learning'''

    def __init__(self, cfg):
        super().__init__(cfg)
        self.n_loops = cfg.n_loops
        self.n_loop_window = cfg.n_loop_window
        
    def _model(self, z, x):
        z = self.backbone(z + x)
        return z
    
    def forward(self, xs, ys):
        horizon_start = max(0, self.n_loops - self.n_loop_window)
        x = self.create_prompt(xs, ys)
        x = self.read_in(x)
        z = torch.zeros_like(x)
        preds = []
        for i in range(self.n_loops):
            if i < horizon_start:
                with torch.no_grad(): z = self._model(z, x)
                continue
            z = self._model(z, x)
            y = self.read_out(z).squeeze(-1)
            preds.append(y[:, ::self.freq])
            if self.cfg.keep_n_tokens: 
                z = z[:, -self.cfg.keep_n_tokens:]
                x = x[:, -self.cfg.keep_n_tokens:]
        return torch.stack(preds) if self.training else preds[-1] # for evaluation, authors only use the last prediction

def loop_loss(preds, ys): return F.mse_loss(preds, ys.expand_as(preds))

# %% ../nbs/02_models.ipynb 5
def get_model(cfg):
    models = {
        'gpt2': Transformer,
        'gpt2_loop': LoopedTransformer
    }
    return models[cfg.family](cfg)

def get_loss(cfg):
    losses = {
        'gpt2': F.mse_loss,
        'gpt2_loop': loop_loss
    }
    return losses[cfg.family]
