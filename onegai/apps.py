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

def uninstall(app):
    shutil.rmtree(f"app/{app}")
    
    return True
