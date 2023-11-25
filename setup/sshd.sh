#!/usr/bin/bash

sudo apt install -y openssh-server

sudo sed -i -e "s/^#Port 22/Port 58022/" /etc/ssh/sshd_config

sudo systemctl start sshd
