#picam is a collection of scripts for the raspberry pi camera. The scripts uses the pi-camera to take pictures when motion is detected.

FEATURES
The SW saves pictures on local directory or a usb flash drive, if a drive can be detected.
Raspberry pi shuts down when the maximum limit of pictures or session time is reached.
If Raspberry pi is connected to internet (wired or wireless), it will update pi but no pictures will be taken.

Install SImpleCV and it's dependencies
Install picamera 

HOW TO INSTALL (as a pi user):
Create the following directories...
#mkdir /home/pi/cam/pics
#mkdir /home/pi/cam/data
#mkdir /home/pi/cam/code

#Download the master.zip to a temporary directory (tmp). 
cd /home/pi/tmp
wget https://github.com/tomasBjornfot/picam/archive/master.zip
''gunzip  master.zip
cp picam-master/*.sh /home/pi/cam/code
cp picam-master/*.py /home/pi/cam/code
cp settings.txt /home/pi/cam/data

# Set scripts as excecutables
sudo chmod +x /home/pi/cam/code/*

#Set start.sh as a startup script. sudo crontab -e 
#Add the following line at the end of the file: @''restart /home/pi/cam/code/start.sh 

#Get network access to pics and data directories
