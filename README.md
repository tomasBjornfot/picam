###PICAM
picam is a collection of scripts for the raspberry pi camera. The scripts uses the pi-camera to take pictures when motion is detected. The scripts are used to make a camera applicaition to take pictures of wild animals. The picamera can be operated without monitor, mouse and keyboard. No knowlage of Linux or computer science is needed.

###FEATURES
The camera takes pictures when a motion is detected. The SW saves pictures on local directory or a usb flash drive. Raspberry pi shuts down when the maximum limit of pictures or session time is reached. If Raspberry pi is connected to internet (wired or wireless), no pictures wil be taken. Instead, the software will be updated.

###PREREQUISITES
* Install SimpleCV: http://www.simplecv.org/
* Install picamera: https://picamera.readthedocs.org/en/release-1.10/install2.html#raspbian-installation 

###INSTALLATION
Create the directories:
```bash
mkdir /home/pi/cam/
mkdir /home/pi/cam/pics
mkdir /home/pi/cam/data
mkdir /home/pi/cam/code
```
Download the master.zip to a temporary directory (tmp):
```bash
cd /home/pi/tmp
wget https://github.com/tomasBjornfot/picam/archive/master.zip
```
Unzip and move the files:
```bash
unzip  master.zip
mv picam-master/*.sh /home/pi/cam/code
mv picam-master/*.py /home/pi/cam/code
mv settings.txt /home/pi/cam/data
```
Set scripts as excecutables:
```bash
sudo chmod +x /home/pi/cam/code/*
```
Set start.sh as a startup script. 
```bash
sudo crontab -e
```
Now, add the following line at the end of the file: 
```bash
@reboot /home/pi/cam/code/start.sh 
```
##NETWORK ACCESS (LAN)
