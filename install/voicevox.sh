#!/usr/bin/bash

python3.11 -V || {
	bash ../setup/python311.sh
}

git clone https://github.com/VOICEVOX/voicevox_engine voicevox
cd voicevox

python3.11 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

venv/bin/python -m pip install -r requirements.txt

wget https://github.com/VOICEVOX/voicevox_engine/releases/download/0.14.6/voicevox_engine-linux-nvidia-0.14.6.7z.001
7z x voicevox_engine-linux-nvidia-0.14.6.7z.001
rm voicevox_engine-linux-nvidia-0.14.6.7z.001

# voicevox_core
#wget https://github.com/VOICEVOX/voicevox_core/releases/latest/download/download.sh
#bash ./download.sh --device cuda
#rm ./download.sh
#venv/bin/python -m pip install https://github.com/VOICEVOX/voicevox_core/releases/download/0.14.5/voicevox_core-0.14.5+cuda-cp38-abi3-linux_x86_64.whl
