#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import time,os,sys,picamera,picamera.array,io,glob
import numpy as np
from math import sqrt
from SimpleCV import Image, Display, Color

""" ************* set date ************* """
def setDate():
    date = time.strftime('%Y%m%d')+'_'+time.strftime('%H%M%S')
    return date
""" ************* read settings ************* """
def readSetting(inSetting):
    file = open('/home/pi/cam/data/settings.txt','r')
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
    return Image( stream.array ).rotate90().rotate(180)
""" ************** comapre images *************** """
def compareImages(img1,img2):
    diffImg = img1.scale(0.5).grayscale() - img2.scale(0.5).grayscale()
    matrix = diffImg.getNumpy()
    flat = matrix.flatten()
    num_change = np.sum(flat)
    return int(100*float(num_change)/float(len(flat)))
""" ******************* set path *********************** """
def setPath():
    devices = glob.glob('/dev/sd?[0-9]')
    if (len(devices)==0):
	os.system("echo 'no usb connected.' >> /home/pi/cam/data/log.txt")
	path = '/home/pi/cam/bilder'
    else:
	os.system("echo 'usb connected.' >> /home/pi/cam/data/log.txt")
	d = devices[-1]
	path = '/mnt/usb'
	os.system('sudo mount -t vfat '+str(devices[-1])+' '+path)
    os.chdir(path)
""" ******************* MAIN *************************** """
os.system("echo 'starts motion.py' >> /home/pi/cam/data/log.txt")
setPath()
mode = str(readSetting('cameraMode'))
res = str(readSetting('cameraResolution'))
noImages = int(readSetting('noImages'))
sessionTime = int(readSetting('sessionTime'))
shutDownWhenDone = str(readSetting('shutDownWhenDone'))
wait = int(readSetting('waitTime'))
detectLimit = int(readSetting('detectLimit'))

noTimes = 0
noIterations = 0
timeStart = int(time.time())

date = setDate()
cam = picamera.PiCamera()
setCamera(cam,mode,res)
refImage = takeImage(cam)

infoFile = open(date+'.txt','w')
infoFile.write("CAMERA:\n")
infoFile.write("Resolution: "+str(cam.resolution)+'\n')
infoFile.write("Exposure mode: "+str(cam.exposure_mode)+'\n')
infoFile.write("Detection limit:"+str(detectLimit)+'\n')
infoFile.write("\nIMAGES:\n")

os.system("echo 'Resolution: "+str(cam.resolution)+"\' >>  /home/pi/cam/data/log.txt")
os.system("echo 'Exposure mode: "+str(cam.exposure_mode)+"\' >>  /home/pi/cam/data/log.txt")
os.system("echo 'Detection limit: "+str(detectLimit)+"\' >>  /home/pi/cam/data/log.txt")
os.system("echo 'Number of images: "+str(noImages)+"\' >>  /home/pi/cam/data/log.txt")
os.system("echo 'Session time: "+str(sessionTime)+"\' >>  /home/pi/cam/data/log.txt")

while (noTimes < noImages and int(time.time())-timeStart<60*sessionTime):
	time.sleep(wait)
	noIterations = noIterations + 1
        newImage = takeImage(cam)
        diff = compareImages(refImage,newImage)
        info = "diff="+str(diff)+" number="+str(noTimes)+" iteration="+str(noIterations)+" time="+str(time.strftime('%H%M%S'))
        print info
	if (diff > detectLimit):
            print "motion detected..."
            newImage.save('motion_'+date+'_'+str(noTimes)+'.png')
	    infoFile.write(info+'\n')
            refImage = newImage
            noTimes = noTimes + 1
infoFile.close()
if (shutDownWhenDone == "True"):
	print "shutting down in 5 minutes..."
	time.sleep(300)
	os.system('sudo shutdown -h now')                     
cam.close()
print "done..."                            
                
