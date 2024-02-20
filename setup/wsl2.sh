#!/usr/bin/bash

if [ ! -f /etc/wsl.conf ]; then
  sudo sh -c 'echo "[boot]\n" > /etc/wsl.conf'
  sudo sh -c 'echo "systemd=true\n" >> /etc/wsl.conf'
fi

if grep -q ~/.bashrc <<< "LD_LIBRARY_PATH=/usr/lib/wsl/lib"; then
  sed -i '1iexport LD_LIBRARY_PATH=/usr/lib/wsl/lib:$LD_LIBRARY_PATH\n' ~/.bashrc
  source ~/.bashrc
fi
