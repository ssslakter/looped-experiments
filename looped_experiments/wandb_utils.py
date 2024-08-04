import wandb

default_filters = [lambda r: r.state != 'running',
                   lambda r: 'curriculum' in r.config['model'],
                   lambda r: r.config['model']['family'] == "gpt2_loop"
                   ]


def get_runs(project, filters=default_filters):
    api = wandb.Api()
    runs = {}
    for r in api.runs(project):
        for f in filters:
            if not f(r): break
        else: runs[r.name] = r
    return runs


def refresh_models(runs, root='../'):
    for r in runs:
        files = filter(lambda f: 'results' in str(f), r.files())
        try:
            model = list(files)[0]
            model.download(root, exist_ok=True)
        except Exception: pass
