#!/usr/bin/bash

git clone https://github.com/VOICEVOX/voicevox_engine voicevox
cd voicevox

python3 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

# requirements.txt for python 3.10
venv/bin/python -m pip install aiofiles==0.7.0
venv/bin/python -m pip install anyio==3.7.1
venv/bin/python -m pip install asgiref==3.7.2
venv/bin/python -m pip install certifi==2023.7.22
venv/bin/python -m pip install cffi==1.15.1
venv/bin/python -m pip install charset-normalizer==3.2.0
venv/bin/python -m pip install click==8.1.7
venv/bin/python -m pip install cython==0.29.36
venv/bin/python -m pip install fastapi==0.103.2
venv/bin/python -m pip install h11==0.14.0
venv/bin/python -m pip install idna==3.4
venv/bin/python -m pip install jinja2==3.1.2
venv/bin/python -m pip install markupsafe==2.1.3
venv/bin/python -m pip install numpy==1.25.2
venv/bin/python -m pip install platformdirs==3.10.0
venv/bin/python -m pip install pycparser==2.21
venv/bin/python -m pip install pydantic==1.10.12
venv/bin/python -m pip install git+https://github.com/VOICEVOX/pyopenjtalk@b35fc89fe42948a28e33aed886ea145a51113f88
venv/bin/python -m pip install python-multipart==0.0.5
venv/bin/python -m pip install pyworld==0.3.4
venv/bin/python -m pip install pyyaml==6.0.1
venv/bin/python -m pip install requests==2.31.0
venv/bin/python -m pip install semver==3.0.1
venv/bin/python -m pip install six==1.16.0
venv/bin/python -m pip install sniffio==1.3.0
venv/bin/python -m pip install soundfile==0.12.1
venv/bin/python -m pip install soxr==0.3.6
venv/bin/python -m pip install starlette==0.27.0
venv/bin/python -m pip install tqdm==4.66.1
venv/bin/python -m pip install typing-extensions==4.7.1
venv/bin/python -m pip install urllib3==2.0.4
venv/bin/python -m pip install uvicorn==0.15.0

wget https://github.com/VOICEVOX/voicevox_engine/releases/download/0.14.6/voicevox_engine-linux-nvidia-0.14.6.7z.001
7z x voicevox_engine-linux-nvidia-0.14.6.7z.001
rm voicevox_engine-linux-nvidia-0.14.6.7z.001

# voicevox_core
#wget https://github.com/VOICEVOX/voicevox_core/releases/latest/download/download.sh
#bash ./download.sh --device cuda
#rm ./download.sh
#venv/bin/python -m pip install https://github.com/VOICEVOX/voicevox_core/releases/download/0.14.5/voicevox_core-0.14.5+cuda-cp38-abi3-linux_x86_64.whl
