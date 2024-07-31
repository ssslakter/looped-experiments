from hydra import compose, initialize
from omegaconf import OmegaConf as oc 


def get_config(path="../configs", overrides=None):
    with initialize(config_path=path, version_base=None):
        return compose("config", overrides)
    
def show_config(cfg, prefix=None):
    print(prefix+oc.to_yaml(cfg, resolve=True))