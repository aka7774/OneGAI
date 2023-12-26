#!/usr/bin/bash

if [ ! -e venv ]; then
  bash setup/wsl2.sh
  bash setup/onegai.sh
fi

venv/bin/python -m gunicorn -w 4 -t 0 -b 0.0.0.0:$1 -k uvicorn.workers.UvicornWorker main:app
