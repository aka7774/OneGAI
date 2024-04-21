import os
import json

from onegai.config import cfg

def clean():
    os.makedirs(cfg['nginx_conf_dir'], exist_ok=True)
    for filename in os.listdir(cfg['nginx_conf_dir']):
        if not filename.startswith('onegai_'):
            continue
        os.remove(f"{cfg['nginx_conf_dir']}/{filename}")

def output():
    with open('nginx.conf', 'r', encoding='utf-8') as f:
        nginx = f.read()

    for app_name in cfg['apps'].keys():
        if not 'https_port' in cfg['apps'][app_name]:
            continue

        with open(f"{cfg['nginx_conf_dir']}/onegai_{app_name}.conf", 'w', encoding='utf-8') as f:
            f.write(nginx.format(
                domain=cfg['domain'],
                port=cfg['apps'][app_name]['port'],
                https_port=cfg['apps'][app_name]['https_port'],
                ))
