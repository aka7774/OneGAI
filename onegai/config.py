import os
import json

config_path = './config.json'
apps_json_path = './apps.json'

cfg = {}
if os.path.exists(config_path):
    with open(config_path, 'r') as f:
        cfg = json.load(f)

cfg_default = {
    "onegai_port": 58080,
    "assign_port": 58081,
    "apps_dir": "..",
    "apps": {
    },
    "_": ""
}

for k, v in cfg_default.items():
    cfg.setdefault(k, v)

del cfg['_']
cfg['_'] = ''

with open(config_path, 'w', encoding='utf-8') as f:
    json.dump(cfg, f, indent=4)

# merge apps.json
apps = {}
if os.path.exists(apps_json_path):
    with open(apps_json_path, 'r') as f:
        apps = json.load(f)

apps.update(cfg['apps'])
cfg['apps'] = apps
del apps
