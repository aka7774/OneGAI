cd apps/

git clone https://github.com/w-okada/voice-changer.git vcclient
cd vcclient

python3 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

venv/bin/pip install -r server/requirements.txt
venv/bin/pip install fairseq pyworld
