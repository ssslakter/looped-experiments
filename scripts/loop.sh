# default short
b=20
T=5
# set curriculum type
clm="log" 
base=2 # for log curriculum we can set base (see ../looped_experiments/curriculum.py)
python main.py "wandb.name=loop_L1_b${b}_T${T}_${clm}_${base}" wandb.enabled=true \
    model=loop \
    model.n_loop_window=$T \
    model.curriculum.loops.start=$T \
    model.curriculum.loops.end=$b \
    model.curriculum.loops.type=$clm \
    training.curriculum.dims.type=$clm \
    training.curriculum.points.type=$clm \
    +training.curriculum.points.kwargs.base=$base \
    +training.curriculum.dims.kwargs.base=$base \
    +model.curriculum.loops.kwargs.base=$base
