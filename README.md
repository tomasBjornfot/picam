# picam
This is a collection of scripts for the raspberry pi camera. The scripts uses the pi-camera to take pictures when motion is detected.

HOW TO INSTALL (as a pi user):
create the following directories...
/home/pi/cam/pics
/home/pi/cam/data
/home/pi/cam/code

Download the master.zip to a temporary directory (tmp). 
cd /home/pi/tmp
wget '''address
''gunzip  master.zip
cd picam-master
cp *.sh $HOME/cam/code
cp *.py $HOME/cam/code
cp settings.txt $HOME/cam/data

Set start.sh as a startup script.
sudo crontab -e 
Add the following line at the end of the file
@''restart /home/pi/ 
