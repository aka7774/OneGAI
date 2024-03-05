#!/usr/bin/bash

git clone https://github.com/litagin02/rvc-tts-webui rvctts
cd rvctts

python3 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

curl -L -O https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/hubert_base.pt
curl -L -O https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/rmvpe.pt

venv/bin/pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
venv/bin/pip install edge-tts
venv/bin/pip install -r requirements.txt

# models
#git clone https://huggingface.co/litagin/rvc_okiba
#cp -r rvc_okiba/models/* weights/
