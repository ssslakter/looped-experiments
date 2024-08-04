# Autogenerated by nbdev

d = { 'settings': { 'branch': 'main',
                'doc_baseurl': '/looped-experiments',
                'doc_host': 'https://ssslakter.github.io',
                'git_url': 'https://github.com/ssslakter/looped-experiments',
                'lib_path': 'looped_experiments'},
  'syms': { 'looped_experiments.all': {},
            'looped_experiments.curriculum': { 'looped_experiments.curriculum.Curriculum': ( '03.1_curriculum.html#curriculum',
                                                                                             'looped_experiments/curriculum.py'),
                                               'looped_experiments.curriculum.Curriculum.__call__': ( '03.1_curriculum.html#curriculum.__call__',
                                                                                                      'looped_experiments/curriculum.py'),
                                               'looped_experiments.curriculum.Curriculum.__init__': ( '03.1_curriculum.html#curriculum.__init__',
                                                                                                      'looped_experiments/curriculum.py'),
                                               'looped_experiments.curriculum.Curriculum.clm_func': ( '03.1_curriculum.html#curriculum.clm_func',
                                                                                                      'looped_experiments/curriculum.py'),
                                               'looped_experiments.curriculum.Curriculum.show': ( '03.1_curriculum.html#curriculum.show',
                                                                                                  'looped_experiments/curriculum.py'),
                                               'looped_experiments.curriculum.CurriculumCB': ( '03.1_curriculum.html#curriculumcb',
                                                                                               'looped_experiments/curriculum.py'),
                                               'looped_experiments.curriculum.CurriculumCB.__init__': ( '03.1_curriculum.html#curriculumcb.__init__',
                                                                                                        'looped_experiments/curriculum.py'),
                                               'looped_experiments.curriculum.CurriculumCB.after_batch': ( '03.1_curriculum.html#curriculumcb.after_batch',
                                                                                                           'looped_experiments/curriculum.py'),
                                               'looped_experiments.curriculum.CurriculumCB.update_task': ( '03.1_curriculum.html#curriculumcb.update_task',
                                                                                                           'looped_experiments/curriculum.py'),
                                               'looped_experiments.curriculum.LoopCB': ( '03.1_curriculum.html#loopcb',
                                                                                         'looped_experiments/curriculum.py'),
                                               'looped_experiments.curriculum.LoopCB.after_batch': ( '03.1_curriculum.html#loopcb.after_batch',
                                                                                                     'looped_experiments/curriculum.py'),
                                               'looped_experiments.curriculum.LoopCB.update_model': ( '03.1_curriculum.html#loopcb.update_model',
                                                                                                      'looped_experiments/curriculum.py'),
                                               'looped_experiments.curriculum.cos_clm': ( '03.1_curriculum.html#cos_clm',
                                                                                          'looped_experiments/curriculum.py'),
                                               'looped_experiments.curriculum.linear_clm': ( '03.1_curriculum.html#linear_clm',
                                                                                             'looped_experiments/curriculum.py'),
                                               'looped_experiments.curriculum.log_clm': ( '03.1_curriculum.html#log_clm',
                                                                                          'looped_experiments/curriculum.py'),
                                               'looped_experiments.curriculum.sqrt_clm': ( '03.1_curriculum.html#sqrt_clm',
                                                                                           'looped_experiments/curriculum.py')},
            'looped_experiments.eval': { 'looped_experiments.eval.MetricsCB': ('eval.html#metricscb', 'looped_experiments/eval.py'),
                                         'looped_experiments.eval.MetricsCB.__init__': ( 'eval.html#metricscb.__init__',
                                                                                         'looped_experiments/eval.py'),
                                         'looped_experiments.eval.MetricsCB.after_batch': ( 'eval.html#metricscb.after_batch',
                                                                                            'looped_experiments/eval.py'),
                                         'looped_experiments.eval.MetricsCB.after_epoch': ( 'eval.html#metricscb.after_epoch',
                                                                                            'looped_experiments/eval.py'),
                                         'looped_experiments.eval.MetricsCB.before_fit': ( 'eval.html#metricscb.before_fit',
                                                                                           'looped_experiments/eval.py'),
                                         'looped_experiments.eval.aggregate_metrics': ( 'eval.html#aggregate_metrics',
                                                                                        'looped_experiments/eval.py'),
                                         'looped_experiments.eval.eval': ('eval.html#eval', 'looped_experiments/eval.py'),
                                         'looped_experiments.eval.squared_error': ( 'eval.html#squared_error',
                                                                                    'looped_experiments/eval.py')},
            'looped_experiments.main': {},
            'looped_experiments.models': { 'looped_experiments.models.LoopedTransformer': ( 'models.html#loopedtransformer',
                                                                                            'looped_experiments/models.py'),
                                           'looped_experiments.models.LoopedTransformer.__init__': ( 'models.html#loopedtransformer.__init__',
                                                                                                     'looped_experiments/models.py'),
                                           'looped_experiments.models.LoopedTransformer._model': ( 'models.html#loopedtransformer._model',
                                                                                                   'looped_experiments/models.py'),
                                           'looped_experiments.models.LoopedTransformer.forward': ( 'models.html#loopedtransformer.forward',
                                                                                                    'looped_experiments/models.py'),
                                           'looped_experiments.models.MaskedTransformer': ( 'models.html#maskedtransformer',
                                                                                            'looped_experiments/models.py'),
                                           'looped_experiments.models.MaskedTransformer.__init__': ( 'models.html#maskedtransformer.__init__',
                                                                                                     'looped_experiments/models.py'),
                                           'looped_experiments.models.MaskedTransformer.forward': ( 'models.html#maskedtransformer.forward',
                                                                                                    'looped_experiments/models.py'),
                                           'looped_experiments.models.Transformer': ( 'models.html#transformer',
                                                                                      'looped_experiments/models.py'),
                                           'looped_experiments.models.Transformer.__init__': ( 'models.html#transformer.__init__',
                                                                                               'looped_experiments/models.py'),
                                           'looped_experiments.models.Transformer.add_positional': ( 'models.html#transformer.add_positional',
                                                                                                     'looped_experiments/models.py'),
                                           'looped_experiments.models.Transformer.create_prompt': ( 'models.html#transformer.create_prompt',
                                                                                                    'looped_experiments/models.py'),
                                           'looped_experiments.models.Transformer.forward': ( 'models.html#transformer.forward',
                                                                                              'looped_experiments/models.py'),
                                           'looped_experiments.models.get_loss': ('models.html#get_loss', 'looped_experiments/models.py'),
                                           'looped_experiments.models.get_model': ('models.html#get_model', 'looped_experiments/models.py'),
                                           'looped_experiments.models.init_all_params': ( 'models.html#init_all_params',
                                                                                          'looped_experiments/models.py'),
                                           'looped_experiments.models.init_weights': ( 'models.html#init_weights',
                                                                                       'looped_experiments/models.py'),
                                           'looped_experiments.models.loop_loss': ( 'models.html#loop_loss',
                                                                                    'looped_experiments/models.py')},
            'looped_experiments.nano_gpt': {},
            'looped_experiments.tasks': { 'looped_experiments.tasks.DataGenerator': ( 'tasks.html#datagenerator',
                                                                                      'looped_experiments/tasks.py'),
                                          'looped_experiments.tasks.DataGenerator.__init__': ( 'tasks.html#datagenerator.__init__',
                                                                                               'looped_experiments/tasks.py'),
                                          'looped_experiments.tasks.DataGenerator.__iter__': ( 'tasks.html#datagenerator.__iter__',
                                                                                               'looped_experiments/tasks.py'),
                                          'looped_experiments.tasks.DataGenerator.__len__': ( 'tasks.html#datagenerator.__len__',
                                                                                              'looped_experiments/tasks.py'),
                                          'looped_experiments.tasks.DataGenerator.__next__': ( 'tasks.html#datagenerator.__next__',
                                                                                               'looped_experiments/tasks.py'),
                                          'looped_experiments.tasks.DataGenerator.task': ( 'tasks.html#datagenerator.task',
                                                                                           'looped_experiments/tasks.py'),
                                          'looped_experiments.tasks.LinearRegression': ( 'tasks.html#linearregression',
                                                                                         'looped_experiments/tasks.py'),
                                          'looped_experiments.tasks.LinearRegression.__call__': ( 'tasks.html#linearregression.__call__',
                                                                                                  'looped_experiments/tasks.py'),
                                          'looped_experiments.tasks.LinearRegression.__init__': ( 'tasks.html#linearregression.__init__',
                                                                                                  'looped_experiments/tasks.py'),
                                          'looped_experiments.tasks.LinearRegression._sparse_mask': ( 'tasks.html#linearregression._sparse_mask',
                                                                                                      'looped_experiments/tasks.py'),
                                          'looped_experiments.tasks.dataloader': ('tasks.html#dataloader', 'looped_experiments/tasks.py'),
                                          'looped_experiments.tasks.get_task_cls': ( 'tasks.html#get_task_cls',
                                                                                     'looped_experiments/tasks.py'),
                                          'looped_experiments.tasks.sample': ('tasks.html#sample', 'looped_experiments/tasks.py')},
            'looped_experiments.training': { 'looped_experiments.training.Callback': ( 'training.html#callback',
                                                                                       'looped_experiments/training.py'),
                                             'looped_experiments.training.Callback.__gt__': ( 'training.html#callback.__gt__',
                                                                                              'looped_experiments/training.py'),
                                             'looped_experiments.training.FnCallback': ( 'training.html#fncallback',
                                                                                         'looped_experiments/training.py'),
                                             'looped_experiments.training.FnCallback.__call__': ( 'training.html#fncallback.__call__',
                                                                                                  'looped_experiments/training.py'),
                                             'looped_experiments.training.FnCallback.__init__': ( 'training.html#fncallback.__init__',
                                                                                                  'looped_experiments/training.py'),
                                             'looped_experiments.training.Learner': ( 'training.html#learner',
                                                                                      'looped_experiments/training.py'),
                                             'looped_experiments.training.Learner.__init__': ( 'training.html#learner.__init__',
                                                                                               'looped_experiments/training.py'),
                                             'looped_experiments.training.Learner.callback': ( 'training.html#learner.callback',
                                                                                               'looped_experiments/training.py'),
                                             'looped_experiments.training.Learner.eval': ( 'training.html#learner.eval',
                                                                                           'looped_experiments/training.py'),
                                             'looped_experiments.training.Learner.fit': ( 'training.html#learner.fit',
                                                                                          'looped_experiments/training.py'),
                                             'looped_experiments.training.Learner.one_batch': ( 'training.html#learner.one_batch',
                                                                                                'looped_experiments/training.py'),
                                             'looped_experiments.training.Learner.one_epoch': ( 'training.html#learner.one_epoch',
                                                                                                'looped_experiments/training.py'),
                                             'looped_experiments.training.SaveModelCB': ( 'training.html#savemodelcb',
                                                                                          'looped_experiments/training.py'),
                                             'looped_experiments.training.SaveModelCB.__init__': ( 'training.html#savemodelcb.__init__',
                                                                                                   'looped_experiments/training.py'),
                                             'looped_experiments.training.SaveModelCB.after_batch': ( 'training.html#savemodelcb.after_batch',
                                                                                                      'looped_experiments/training.py'),
                                             'looped_experiments.training.SaveModelCB.after_fit': ( 'training.html#savemodelcb.after_fit',
                                                                                                    'looped_experiments/training.py'),
                                             'looped_experiments.training.TimerCB': ( 'training.html#timercb',
                                                                                      'looped_experiments/training.py'),
                                             'looped_experiments.training.TimerCB.after_batch': ( 'training.html#timercb.after_batch',
                                                                                                  'looped_experiments/training.py'),
                                             'looped_experiments.training.TimerCB.before_batch': ( 'training.html#timercb.before_batch',
                                                                                                   'looped_experiments/training.py'),
                                             'looped_experiments.training.TimerCB.before_fit': ( 'training.html#timercb.before_fit',
                                                                                                 'looped_experiments/training.py'),
                                             'looped_experiments.training.ToDeviceCB': ( 'training.html#todevicecb',
                                                                                         'looped_experiments/training.py'),
                                             'looped_experiments.training.ToDeviceCB.__init__': ( 'training.html#todevicecb.__init__',
                                                                                                  'looped_experiments/training.py'),
                                             'looped_experiments.training.ToDeviceCB.before_batch': ( 'training.html#todevicecb.before_batch',
                                                                                                      'looped_experiments/training.py'),
                                             'looped_experiments.training.ToDeviceCB.before_fit': ( 'training.html#todevicecb.before_fit',
                                                                                                    'looped_experiments/training.py'),
                                             'looped_experiments.training.WandbCB': ( 'training.html#wandbcb',
                                                                                      'looped_experiments/training.py'),
                                             'looped_experiments.training.WandbCB.__init__': ( 'training.html#wandbcb.__init__',
                                                                                               'looped_experiments/training.py'),
                                             'looped_experiments.training.WandbCB.after_batch': ( 'training.html#wandbcb.after_batch',
                                                                                                  'looped_experiments/training.py'),
                                             'looped_experiments.training.WandbCB.after_fit': ( 'training.html#wandbcb.after_fit',
                                                                                                'looped_experiments/training.py'),
                                             'looped_experiments.training.WandbCB.before_fit': ( 'training.html#wandbcb.before_fit',
                                                                                                 'looped_experiments/training.py'),
                                             'looped_experiments.training.repr_cbs': ( 'training.html#repr_cbs',
                                                                                       'looped_experiments/training.py'),
                                             'looped_experiments.training.with_cbs': ( 'training.html#with_cbs',
                                                                                       'looped_experiments/training.py'),
                                             'looped_experiments.training.with_cbs.__call__': ( 'training.html#with_cbs.__call__',
                                                                                                'looped_experiments/training.py'),
                                             'looped_experiments.training.with_cbs.__init__': ( 'training.html#with_cbs.__init__',
                                                                                                'looped_experiments/training.py')},
            'looped_experiments.utils': {},
            'looped_experiments.wandb_utils': {}}}
