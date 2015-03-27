#!/bin/bash
echo "starts camera..."
cd /home/pi/cam/code
sudo ./motion.py
sudo umount /mnt/usb
