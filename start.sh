#!/bin/bash
LOG=$HOME/cam/data/log.txt
echo "**********"$(date)"**********" >> $LOG
echo "starts start.sh" >> $LOG

VAR=$(ping www.google.se -c 5 | grep "0% packet loss")
if [ -z $VAR ]; then
	echo "no internet connection found" >> $LOG
	cd /home/pi/cam/code
	sudo ./motion.py
	sudo umount /mnt/usb
else
	echo "internet connection found" >> $LOG
	./updatecam.sh
fi
echo "start.sh end" >> $LOG
exit 0
