from hydra import compose, initialize
from omegaconf import OmegaConf as oc
from torch import Tensor
import torch


def get_config(path="../configs", overrides=None):
    with initialize(config_path=path, version_base=None):
        return compose("config", overrides)


def show_config(cfg, prefix=''):
    print(prefix + oc.to_yaml(cfg, resolve=True))


def get_default_device():
    is_cuda = torch.cuda.is_available()
    return torch.device("cuda" if is_cuda else "cpu")


def_device = get_default_device()


def to_cpu(x):
    if isinstance(x, Tensor):
        return x.detach().cpu()
    else:
        return to_device(x, "cpu")


def to_device(x, device=def_device):
    if isinstance(x, Tensor):
        return x.to(device)
    elif isinstance(x, dict):
        return {k: to_device(v, device) for k, v in x.items()}
    elif isinstance(x, list):
        return [to_device(v, device) for v in x]
    elif isinstance(x, tuple):
        return tuple(to_device(v, device) for v in x)
    else: return x
