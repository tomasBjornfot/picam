#!/bin/bash

mv start.sh /home/pi/picam/code
mv updatecam.sh /home/pi/picam/code
mv *.py /home/pi/picam/code
mv settings.txt /home/pi/picam/data
cd ..
chmod 666 settings.txt
rm -r picam-master

cd /home/pi/picam/code
chmod +x *

