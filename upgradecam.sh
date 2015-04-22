#!/bin/bash

mv *.sh /home/pi/picam/code
mv *.py /home/pi/picam/code
mv settings.txt /home/pi/picam/data
cd ..
rm -r picam-master

cd /home/pi/picam/code
chmod +x *
