#!/usr/bin/bash

bash setup/venv.sh

#venv/bin/python -m pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118

venv/bin/python -m pip install gradio_client gunicorn uvicorn fastapi soundfile psutil pytest pytest-check sqlalchemy numpy
