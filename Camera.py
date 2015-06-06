#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import time,os,sys,picamera,picamera.array,io,glob
import numpy as np
from math import fabs
from SimpleCV import Image, Display, Color

class Camera:
	""" ************ constructor ********** """
	def __init__(self):
		self.cam = picamera.PiCamera()
		self.stream = picamera.array.PiRGBArray(self.cam)
		self.path = setPath()
		self.date = setDate()
		
		#reads general settings from settings.txt
		self.photoMode = str(readSetting('photoMode'))
		self.waitStart = int(readSetting('waitStart'))
		self.waitTime = int(readSetting('waitTime'))
		self.waitEnd = int(readSetting('waitEnd'))
		self.cameraResolution = str(readSetting('cameraResolution'))
		self.noImages = int(readSetting('noImages'))
		self.sessionTime = int(readSetting('sessionTime'))
		self.shutDownWhenDone = str(readSetting('shutDownWhenDone'))
		
		# reads motion specific settings from settings.txt
		self.cameraMode = str(readSetting('cameraMode'))
		self.detectLimit = int(readSetting('detectLimit'))
		
	""" ************* set date ************* """
	def setDate():
		date = time.strftime('%Y%m%d')+'_'+time.strftime('%H%M%S')
		return date
	""" ************* read settings ************* """
	def readSetting(inSetting):
		file = open('/home/pi/picam/data/settings.txt','r')
		lines = file.readlines()
		for line in lines:
		# skip line if comment
			if line[0] == '#':
				continue
			setting = line.split('=')
			if (setting[0]== inSetting):
	return setting[1].rstrip('\n')
	return 'null'
	""" ************* set camera ************* """
	def setCamera(self):
		#print "sets camera parameters"
		if (self.cameraResolution == "high"):
			self.cam.resolution = cam.MAX_IMAGE_RESOLUTION
		if (self.cameraResolution == "mid"):
			self.cam.resolution = (1600,1200)
		if (self.cameraResolution == "low"):
			self.cam.resolution = (800,600)
	self.cam.exposure_mode = self.cameraMode
	print "camera resolution:", self.cam.resolution
	print "exposure mode:",self.cam.exposure_mode
	""" ************** take image *************** """
	def takeImage(self):
		self.cam.capture(stream, format='rgb')
		return Image( stream.array ).rotate90()
	""" ************** comapre images *************** """
	def compareImages(img1,img2,diffSize):
		img1 = img1.scale(diffSize)
		img2 = img2.scale(diffSize)
		diffImg = img1 - img2
		return int(100.0/256.0*sum(diffImg.meanColor()))
	""" ******************* set path *********************** """
	def setPath(self):
		devices = glob.glob('/dev/sd?[0-9]')
		if (len(devices)==0):
			os.system("echo 'no usb connected.' >> /home/pi/picam/data/log.txt")
			self.path = '/home/pi/picam/pics'
		else:
			os.system("echo 'usb connected.' >> /home/pi/picam/data/log.txt")
			d = devices[-1]
			self.path = '/mnt/usb'
		os.system('sudo mount -t vfat '+str(devices[-1])+' '+path)
		os.chdir(self.path)
	""" ******************* MAIN *************************** """
	def motion(self):
		time.sleep(waitStart*60)
		os.system("echo 'starts motion.py' >> /home/pi/picam/data/log.txt")

		noTimes = 0
		noIterations = 0
		timeStart = int(time.time())
		
		setCamera()
		refImage = takeImage()

		infoFile = open(date+'.txt','w')
		infoFile.write("CAMERA:\n")
		infoFile.write("Resolution: "+str(cam.resolution)+'\n')
		infoFile.write("Exposure mode: "+str(cam.exposure_mode)+'\n')
		infoFile.write("Detection limit:"+str(self.detectLimit)+'\n')
		infoFile.write("\nIMAGES:\n")

		os.system("echo 'Resolution: "+str(self.cam.resolution)+"\' >>  /home/pi/picam/data/log.txt")
		os.system("echo 'Exposure mode: "+str(self.cam.exposure_mode)+"\' >>  /home/pi/picam/data/log.txt")
		os.system("echo 'Detection limit: "+str(self.detectLimit)+"\' >>  /home/pi/picam/data/log.txt")
		os.system("echo 'Number of images: "+str(self.noImages)+"\' >>  /home/pi/picam/data/log.txt")
		os.system("echo 'Session time: "+str(self.sessionTime)+"\' >>  /home/pi/picam/data/log.txt")
		os.system("echo 'wait time: "+str(self.waitTime)+"\' >>  /home/pi/picam/data/log.txt")
		os.system("echo 'wait start: "+str(self.waitStart)+"\' >>  /home/pi/picam/data/log.txt")

		while (noTimes < noImages and int(time.time())-timeStart<60*self.sessionTime):
			time.sleep(self.waitTime)
			noIterations = noIterations + 1
			newImage = takeImage()
			diff = compareImages(refImage,newImage,0.1)
			info = "Picture="+str(noTimes)+" DetectionValue="+str(diff)+" iteration="+str(noIterations)+" time="+str(time.strftime('%H%M%S'))
			print info
			if (diff > self.detectLimit):
				print "motion detected..."
				newImage.save('motion_'+self.date+'_'+str(noTimes)+'.png')
				infoFile.write(info+'\n')
        			noTimes = noTimes + 1
				refImage = newImage
				infoFile.close()
		self.cam.close()
		if (shutDownWhenDone == "True"):
		print "shutting down in",str(self.waitEnd),"minutes..."
		time.sleep(60*self.waitEnd)
		os.system('sudo shutdown -h now')                     
		print "done..."
