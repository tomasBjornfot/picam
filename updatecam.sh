#!/bin/bash
LOG=/home/pi/picam/data/log.txt
echo "updates pi.." >> $LOG
sudo apt-get update
sudo apt-get upgrade -y

echo "gets camera scripts from github to /data/picam-master.." >> $LOG
cd /home/pi/picam/data
rm -r picam-master
wget https://github.com/tomasBjornfot/picam/archive/master.zip
unzip master.zip
rm master.zip
sudo chmod 777 picam-master/*
exit 0
