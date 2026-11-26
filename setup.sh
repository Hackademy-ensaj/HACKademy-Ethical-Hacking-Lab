#!/bin/bash
set -e
sudo apt update
sudo apt install -y git nmap curl dnsutils python3 john
echo "HACKademy Ethical Hacking Lab ready!"
echo "Ensuite : bash start-target.sh"
