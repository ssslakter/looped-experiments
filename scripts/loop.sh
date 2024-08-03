# default short
b=20
T=5
clm=cos
python main.py "wandb.name=LR_loop_L1_ends\{$b\}_T\{$T\}_$clm" wandb.enabled=true \
 model=loop training=loop \
 model.n_embd=128 \
 model.n_dims=10 \
 model.n_loop_window=$T \
 model.curriculum.loops.start=$T \
 model.curriculum.loops.end=$b \
 model.curriculum.loops.interval=300 \
 model.repeat_positional=false \
 model.repeat_ln=false \
 training.learning_rate=0.0002 \
 training.train_steps=5000 \
 training.n_epoch=20 \
 training.batch_size=128 \
 model.curriculum.loops.type=$clm \
 training.curriculum.dims.type=$clm \
 training.curriculum.points.type=$clm