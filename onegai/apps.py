import os
import shutil
import psutil
import json
import subprocess
import time
import gc

from onegai.config import cfg

def get_apps_dir():
    return os.path.abspath(cfg['apps_dir'])

def get_onegai_dir():
    return os.path.abspath('.')

def get_installed():
    return os.listdir(get_apps_dir())

def get_installable():
    installable = []
    for sh in os.listdir('install'):
        if sh == 'old':
            continue
        if sh == 'akaspace.sh':
            continue

        installable.append(os.path.splitext(sh)[0])
        
    return installable

def get_installable_akaspace():
    akaspaces = []
    for app_name in cfg['apps'].keys():
        if 'is_akaspace' in cfg['apps'][app_name] and cfg['apps'][app_name]['is_akaspace']:
            akaspaces.append(app_name)
    return akaspaces

def install(app_name):
    sh = f'{get_onegai_dir()}/install/{app_name}.sh'

    if not os.path.exists(sh):
        return False

    cmd = f'cd "{get_apps_dir()}"; exec bash "{sh}"'
    cp = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(cp.stdout)

    return True

def install_akaspace(app_name):
    if not app_name:
        return False

    sh = f'{get_onegai_dir()}/install/akaspace.sh'

    cmd = f'cd "{get_apps_dir()}"; exec bash "{sh}" {app_name}'
    cp = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(cp.stdout)

    return True

def uninstall(app_name):
    if not app_name:
        return False

    path = f'{get_apps_dir()}/{app_name}'
    if not os.path.exists(path):
        return False

    shutil.rmtree(path)

    return True

def get_cmd(app_name):
    port = cfg['apps'][app_name]['port']
    exec = cfg['apps'][app_name]['exec'].format(port=port)
    cmd = f'cd "{get_apps_dir()}"; {exec}'
    return cmd

def start(app_name, restart = 0):
    if app_name not in cfg['apps']:
        return f"{app_name} not in config apps"

    path = f'{get_apps_dir()}/{app_name}'
    if not os.path.exists(path):
        return f"{app_name} is not installed"

    pid = get_pconn(cfg['apps'][app_name]['port'])
    if pid:
        return f"{app_name} already started {pid}"

    if restart:
        stop(app_name)

    cmd = get_cmd(app_name)
    print(cmd)
    proc = subprocess.Popen(cmd, shell=True, text=True)

    timeout = 30
    i = 0
    while not get_pconn(port):
        time.sleep(1)
        if proc.poll():
            return proc.communicate(),
        i += 1
        if i >= timeout:
            return 'timed out.'

    return ''

def stop(app_name, kill = False):
    if app_name not in cfg['apps']:
        return f"{app_name} not in config apps"

    path = f'{get_apps_dir()}/{app_name}'
    if not os.path.exists(path):
        return f"{app_name} is not installed"

    pid = get_pconn(cfg['apps'][app_name]['port'])

    if not pid:
        return False

    proc = psutil.Process(pid)
    for cpid in [c.pid for c in proc.children(recursive=True)]:
        if kill:
            psutil.Process(cpid).kill()
        else:
            psutil.Process(cpid).terminate()

    if kill:
        proc.kill()
    else:
        proc.terminate()
    gc.collect()

    return True

def get_status_list():
    rs = []
    for app_name in get_installed():
        rs.append(get_status(app_name))
    return rs

def get_status(app_name):
    try:
        port = cfg['apps'][app_name]['port']
        pid = get_pconn(port)
    except:
        port = ''
        pid = ''

    status = [
        app_name,
        bool(app_name in cfg['apps'].keys()),
        port,
        pid,
        ]

    return status

def get_vram():
    cmd = 'nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader,nounits'
    csv = subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout
    vram = csv.split(',')

    available = round((float(vram[1]) - float(vram[0])) / 1024, 3)
    total = round(float(vram[1]) / 1024, 3)

    return (available, total)

def get_ram():
    ram = psutil.virtual_memory()
    available = round(ram.available / 1024 / 1024 / 1024, 3)
    total = round(ram.total / 1024 / 1024 / 1024, 3)

    return (available, total)

def get_pconn(port):
    pid = None
    for pconn in psutil.net_connections():
        if port == pconn.laddr.port:
            pid = pconn.pid
            break

    return pid

def get_lsof_i():
    cmd = 'lsof -iTCP | grep LISTEN'
    result = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
    return result.stdout
