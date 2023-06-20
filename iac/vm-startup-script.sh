#!/bin/bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install python3-pip git stress -y

curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh
sudo bash add-google-cloud-ops-agent-repo.sh --also-install

git clone https://github.com/salimpadela/gcp-monitoring-tutorial.git
cd gcp-monitoring-tutorial
pip install -r requirements.txt
chmod +x app.py
nohup python3 app.py &

