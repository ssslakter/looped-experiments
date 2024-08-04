import wandb


def get_runs(project):
    api = wandb.Api()
    return api.runs(project)
    
def refresh_models(runs, root='../'):
    for r in runs:
        files = filter(lambda f: 'results' in str(f),  r.files())
        model = list(files)[0]
        model.download(root, exist_ok=True)