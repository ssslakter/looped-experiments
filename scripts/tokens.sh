#####################################
# Default looped-transformer with the same number of tokens
#####################################
b=30
T=10
# python main.py "wandb.name=loop_L1_b${b}_T${T}" wandb.enabled=true \
#     model=loop \
#     model.n_loop_window=$T \
#     model.curriculum.loops.start=$T \
#     model.curriculum.loops.end=$b



#####################################
# Decrement tokens by 1 each loop until keep 5 last
#####################################
k=5
d=2
python main.py "wandb.name=loop_L1_b${b}_T${T}_k${k}_d${d}" wandb.enabled=true \
    model=loop \
    model.n_loop_window=$T \
    model.curriculum.loops.start=$T \
    model.curriculum.loops.end=$b \
    model.keep_n_tokens=$k \
    model.token_dec=$d


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
