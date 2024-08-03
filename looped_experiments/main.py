import random
from pathlib import Path

import torch
from hydra import main
from omegaconf import DictConfig

from .all import *

config_path = str((Path(__file__) / '../../configs').resolve())

def set_random(seed):
    random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)

@main(config_path, version_base=None, config_name='config')
def run(cfg: DictConfig):
    show_config(cfg, "Running with config:\n")
    set_random(cfg.random_seed)
    train = cfg.training
    task = get_task_cls(cfg.task.task_name)(train.batch_size, **cfg.task)
    dl_train = dataloader(task, train.train_steps)
    dl_eval = dataloader(task, train.eval_steps)

    model = get_model(cfg.model)
    loss_fn = get_loss(cfg.model)
    @FnCallback("before_batch")
    def trans_input(learner): learner.xb = (learner.xb, learner.yb)

    cbs = [TimerCB(), ToDeviceCB(), 
           SaveModelCB(cfg.out_dir, train.save_every_steps), CurriculumCB(train.curriculum, train), trans_input]
    if cfg.wandb.enabled: cbs.append(WandbCB(cfg))
    if "loop" in cfg.model.family: cbs.append(LoopCB(cfg.model.curriculum, train))
    learn = Learner(model, dl_train, dl_eval, train.n_epoch, wd = train.weight_decay, loss_fn=loss_fn, cbs=cbs)
    print(f"Callbacks used: {repr_cbs(sorted(cbs))}")
    learn.fit(lr=train.learning_rate)

