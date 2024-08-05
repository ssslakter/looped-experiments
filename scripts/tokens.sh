#####################################
# Default looped-transformer with the same number of tokens
#####################################
b=20
T=5
# python main.py "wandb.name=loop_L1_b${b}_T${T}" wandb.enabled=true \
#     model=loop \
#     model.n_loop_window=$T \
#     model.curriculum.loops.start=$T \
#     model.curriculum.loops.end=$b



#####################################
# Decrement tokens by 1 each loop until keep 5 last
#####################################
k=5
d=1
python main.py "wandb.name=loop_L2_b${b}_T${T}_k${k}_d${d}" wandb.enabled=true \
    model=loop \
    model.n_layer=2 \
    model.n_loop_window=$T \
    model.curriculum.loops.start=$T \
    model.curriculum.loops.end=$b \
    model.keep_n_tokens=$k \
    model.token_dec=$d \
    model.repeat_positional=false \
    model.repeat_ln=true


#####################################
# Keep only 5 tokens after first loop
#####################################
k=5
d=100
# python main.py "wandb.name=loop_L1_b${b}_T${T}_k${k}_d${d}" wandb.enabled=true \
#     model=loop \
#     model.n_loop_window=$T \
#     model.curriculum.loops.start=$T \
#     model.curriculum.loops.end=$b \
#     model.keep_n_tokens=$k \
#     model.token_dec=$d
