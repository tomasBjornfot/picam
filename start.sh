#!/bin/bash
sleep 15
LOG=/home/pi/cam/data/log.txt
chown root /home/pi/data/*
chmod 666 /home/pi/cam/data/*
echo "**********"$(date)"**********" >> $LOG
echo "starts start.sh" >> $LOG
cd /home/pi/cam/code
VAR=$(ping www.google.se -c 5 | grep "0% packet loss")
if [ -z $VAR ]; then
	echo "no internet connection found" >> $LOG
	./motion.py
	sudo umount /mnt/usb
else
	echo "internet connection found" >> $LOG
	echo "updates software..." >> $LOG
	./updatecam.sh
	echo "closeIfDisconnected.py..." >> $LOG
	./closeIfDisconnected.py
fi
echo "start.sh ending "$(date) >> $LOG
exit 0
