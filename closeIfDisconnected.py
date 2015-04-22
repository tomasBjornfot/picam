#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import os,time
while True:
	time.sleep(10)
	result = os.system("ping www.google.com -c 5 | grep '0% packet loss'")
	if not result == 0:
		os.system("echo 'No internet connection. shutting down...' >> /home/pi/cam/data/log.txt")
		time.sleep(5)
		os.system("sudo shutdown -h now")
