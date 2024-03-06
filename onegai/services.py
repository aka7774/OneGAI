import os
import importlib
import psutil
import json
import subprocess
import time
import gc

services_json_path = 'services.json'
svc = {}
if os.path.exists(services_json_path):
    with open(services_json_path, 'r') as f:
        svc = json.load(f)

def start(app, restart = 0):
    if 'vram' in svc[app] and svc[app]['vram']:
        (available, total) = get_vram()
        if available < svc[app]['vram']:
            return f"vram available {available} GB require {svc[app]['vram']} GB"

    if 'ram' in svc[app] and svc[app]['ram']:
        (available, total) = get_ram()
        if available < svc[app]['ram']:
            return f"ram available {available} GB require {svc[app]['ram']} GB"

    if svc[app]['type'] in ['webapi', 'gradio']:
        pid = get_pconn(svc[app]['port'])
        if pid:
            return f"already started {pid}"

    if restart:
        stop(app)

    port = svc[app]['port']
    exec = svc[app]['exec'].format(port=port)
    export = ''
    if svc[app]['type'] == 'gradio':
        export = f"export GRADIO_SERVER_PORT={port}; "
    cmd = f"cd apps/{app}; {export}{exec}"
    print(cmd)
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #pid = proc.pid

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

def stop(app):
    pid = get_pconn(svc[app]['port'])

    if not pid:
        return False

    proc = psutil.Process(pid)
    for cpid in [c.pid for c in proc.children(recursive=True)]:
        psutil.Process(cpid).kill()
    proc.kill()
    gc.collect()

    return True

def get_status(app):
    if not app in svc:
        return app
    pid = get_pconn(svc[app]['port'])
    return f"{app}:{svc[app]['port']} pid={pid}"

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
