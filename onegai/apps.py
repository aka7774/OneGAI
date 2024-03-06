import os
import shutil
import psutil
import subprocess

def install(app):
    if not os.path.exists(f"install/{app}.sh"):
        return False

    cmd = f"cd apps; exec bash ../install/{app}.sh"
    cp = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(cp.stdout)

    return True

def install_akaspace(app):
    if not app:
        return False

    cmd = f"cd apps; exec bash ../install/akaspace.sh {app}"
    cp = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(cp.stdout)

    return True

def uninstall(app):
    if not app:
        return False

    path = f"apps/{app}"
    if not os.path.exists(path):
        return False

    shutil.rmtree(path)

    return True
