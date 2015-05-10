###PICAM
Picam is a collection of scripts for the raspberry pi camera. The scripts uses the camera to take pictures when motion is detected. The scripts are used to make a camera applicaition for wild animals. The picamera can be operated without monitor, mouse and keyboard. No knowlage of Linux or computer science is required.

###FEATURES
The camera takes pictures when a motion is detected. The SW saves pictures on local directory or a usb flash drive. Raspberry pi can shut down when the maximum limit of pictures or session time is reached. If Raspberry pi is connected to internet (wired or wireless), no pictures wil be taken. Instead, the software will be updated.

###PREREQUISITES
* Raspian: http://www.raspbian.org/
* SimpleCV: http://www.simplecv.org/
* picamera: https://picamera.readthedocs.org/en/release-1.10/install2.html#raspbian-installation 

###INSTALLATION
Create the directories:
```bash
mkdir /home/pi/picam/
mkdir /home/pi/picam/pics
mkdir /home/pi/picam/data
mkdir /home/pi/picam/code
```
Download the master.zip to a temporary directory (tmp):
```bash
cd /home/pi/tmp
wget https://github.com/tomasBjornfot/picam/archive/master.zip
```
Unzip
```bash
unzip  master.zip
cd picam-master
```
Set upgrade.sh script as executable and execute:
```bash
sudo chmod +x upgrade.sh
sudo ./upgrade.sh
```
Set start.sh as a startup script: 
```bash
sudo crontab -e
```
Add the following line at the end of the crontab file: 
```bash
@reboot /home/pi/picam/code/start.sh 
```
##NETWORK ACCESS (LAN)
Open samba configuration file
```bash
sudo nano /etc/samba/smb.conf
```
Add the following lines at the end of the file:
NOT READY...
