#!/bin/bash

mv *.sh /home/pi/picam/code
mv *.py /home/pi/picam/code
mv settings.txt /home/pi/picam/data

cd /home/pi/picam/code
chmod +x *
