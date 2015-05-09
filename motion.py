#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import time,os,sys,picamera,picamera.array,io,glob
import numpy as np
from math import fabs
from SimpleCV import Image, Display, Color

""" ************* set date ************* """
def setDate():
    date = time.strftime('%Y%m%d')+'_'+time.strftime('%H%M%S')
    return date
""" ************* read settings ************* """
def readSetting(inSetting):
    file = open('/home/pi/picam/data/settings.txt','r')
    lines = file.readlines()
    for line in lines:
	setting = line.split('=')
	if (setting[0]== inSetting):
		return setting[1].rstrip('\n')
    return 'null'
""" ************* set camera ************* """
def setCamera(cam,mode,res):
    #print "sets camera parameters"
    if (res == "high"):
    	cam.resolution = cam.MAX_IMAGE_RESOLUTION
    if (res == "mid"):
    	cam.resolution = (1600,1200)
    if (res == "low"):
	cam.resolution = (800,600)
    cam.exposure_mode = mode
    print "camera resolution:", cam.resolution
    print "exposure mode:",cam.exposure_mode
""" ************** take image *************** """
def takeImage(cam):
    stream = picamera.array.PiRGBArray(cam)
    cam.capture(stream, format='rgb')
    #return Image( stream.array ).rotate90().rotate(180)
    return Image( stream.array ).rotate90()
""" ************** comapre images *************** """
def compareImages_old(img1,img2,diffSize):
    img1 = img1.scale(diffSize).grayscale()
    img2 = img2.scale(diffSize).grayscale()
    diffImg = img1 - img2
    flat = diffImg.getNumpy().flatten()
    flat = np.absolute(flat)
    num_change = np.sum(flat)
    return  int(100*float(num_change)/float(len(flat)))

def compareImages(img1,img2,diffSize):
    img1 = img1.scale(diffSize)
    img2 = img2.scale(diffSize)
    diffImg = img1 - img2
    return int(100.0/256.0*sum(diffImg.meanColor()))
""" ******************* set path *********************** """
def setPath():
    devices = glob.glob('/dev/sd?[0-9]')
    if (len(devices)==0):
	os.system("echo 'no usb connected.' >> /home/pi/picam/data/log.txt")
	path = '/home/pi/picam/pics'
    else:
	os.system("echo 'usb connected.' >> /home/pi/picam/data/log.txt")
	d = devices[-1]
	path = '/mnt/usb'
	os.system('sudo mount -t vfat '+str(devices[-1])+' '+path)
    os.chdir(path)
""" ******************* MAIN *************************** """
os.system("echo 'starts motion.py' >> /home/pi/picam/data/log.txt")
setPath()
date = setDate()
cam = picamera.PiCamera()

#reads general settings from settings.txt
photoMode = int(readSetting('photoMode'))
waitStart = int(readSetting('waitStart'))
waitTime = int(readSetting('waitTime'))
waitEnd = int(readSetting('waitEnd'))
cameraResolution = str(readSetting('cameraResolution'))
noImages = int(readSetting('noImages'))
sessionTime = int(readSetting('sessionTime'))
shutDownWhenDone = str(readSetting('shutDownWhenDone'))

# reads motion specific settings from settings.txt
cameraMode = str(readSetting('cameraMode'))
detectLimit = int(readSetting('detectLimit'))

noTimes = 0
noIterations = 0
timeStart = int(time.time())

setCamera(cam,cameraMode,cameraResolution)
refImage = takeImage(cam)

infoFile = open(date+'.txt','w')
infoFile.write("CAMERA:\n")
infoFile.write("Resolution: "+str(cam.resolution)+'\n')
infoFile.write("Exposure mode: "+str(cam.exposure_mode)+'\n')
infoFile.write("Detection limit:"+str(detectLimit)+'\n')
infoFile.write("\nIMAGES:\n")

os.system("echo 'Resolution: "+str(cam.resolution)+"\' >>  /home/pi/picam/data/log.txt")
os.system("echo 'Exposure mode: "+str(cam.exposure_mode)+"\' >>  /home/pi/picam/data/log.txt")
os.system("echo 'Detection limit: "+str(detectLimit)+"\' >>  /home/pi/picam/data/log.txt")
os.system("echo 'Number of images: "+str(noImages)+"\' >>  /home/pi/picam/data/log.txt")
os.system("echo 'Session time: "+str(sessionTime)+"\' >>  /home/pi/picam/data/log.txt")
os.system("echo 'wait time: "+str(waitTime)+"\' >>  /home/pi/picam/data/log.txt")
os.system("echo 'wait start: "+str(waitStart)+"\' >>  /home/pi/picam/data/log.txt")

time.sleep(waitStart*60)
while (noTimes < noImages and int(time.time())-timeStart<60*sessionTime):
	time.sleep(waitTime)
	noIterations = noIterations + 1
        newImage = takeImage(cam)
        diff = compareImages(refImage,newImage,0.1)
        info = "Picture="+str(noTimes)+" DetectionValue="+str(diff)+" iteration="+str(noIterations)+" time="+str(time.strftime('%H%M%S'))
        print info
	if (diff > detectLimit):
            print "motion detected..."
            newImage.save('motion_'+date+'_'+str(noTimes)+'.png')
	    infoFile.write(info+'\n')
            noTimes = noTimes + 1
	refImage = newImage
infoFile.close()

if (shutDownWhenDone == "True"):
	print "shutting down in",str(waitEnd),"minutes..."
	time.sleep(60*waitEnd)
	os.system('sudo shutdown -h now')                     
cam.close()
print "done..."                            
                                         
                
