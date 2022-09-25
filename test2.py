# Number of training steps.
num_steps = 5000  # 200000
# Number of evaluation steps.
num_eval_steps = 100
MODELS_CONFIG = {
    'ssd_mobilenet_v2': {
        'model_name': 'ssd_mobilenet_v2_coco_2018_03_29',
        'pipeline_file': 'ssd_inception_v2_coco.config',
        'batch_size': 16
    }
}
selected_model = 'ssd_mobilenet_v2'
MODEL = MODELS_CONFIG[selected_model]['model_name']
pipeline_file = MODELS_CONFIG[selected_model]['pipeline_file']
batch_size = MODELS_CONFIG[selected_model]['batch_size']
import os
repo_dir_path = os.path.abspath(os.path.join('.', os.path.basename(repo_url)))


import os
os.environ['PYTHONPATH'] += ':/content/models/research/:/content/models/research/slim/'
