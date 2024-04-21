import os
import json

config_path = './config.json'
apps_json_path = './apps.json'

cfg = {}

def get_apps_dir():
    return os.path.abspath(cfg['apps_dir'])

def get_installed():
    return os.listdir(get_apps_dir())

def get_new_port():
    port = cfg['assign_port']
    while is_used(port):
        port += 1
        
    return port

def is_used(port):
    for app_name in cfg['apps'].keys():
        if not 'port' in cfg['apps'][app_name]:
            continue
        if cfg['apps'][app_name]['port'] == port:
            return True

    return False

def get_apps_json():
    apps = {}
    if os.path.exists(apps_json_path):
        with open(apps_json_path, 'r', encoding='utf-8') as f:
            apps = json.load(f)

    return apps

# get config json
if os.path.exists(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        cfg = json.load(f)

cfg_default = {
    "domain": "",
    "nginx_conf_dir": "nginx_conf",
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

# assign new port
apps = get_apps_json()
for app_name in get_installed():
    if app_name not in cfg['apps'].keys():
        if app_name in apps:
            cfg['apps'][app_name] = apps[app_name]
        else:
            cfg['apps'][app_name] = {}
    if 'port' in cfg['apps'][app_name]:
        continue
    cfg['apps'][app_name]['port'] = get_new_port()

# save config json
with open(config_path, 'w', encoding='utf-8') as f:
    json.dump(cfg, f, indent=4)
