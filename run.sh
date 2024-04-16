#!/usr/bin/bash

if [ ! -e venv ]; then
  bash setup/wsl2.sh
  bash setup/onegai.sh
fi

echo `venv/bin/python get_cmd.py $1` > _.sh
bash _.sh
