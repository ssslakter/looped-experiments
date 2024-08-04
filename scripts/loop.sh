# default short
b=20
T=5
clm=log
python main.py "wandb.name=LR_loop_L1_b${b}_T${T}_${clm}" wandb.enabled=true \
 model=loop \
 model.n_loop_window=$T \
 model.curriculum.loops.start=$T \
 model.curriculum.loops.end=$b \
 model.curriculum.loops.type=$clm \
 training.curriculum.dims.type=$clm \
 training.curriculum.points.type=$clm