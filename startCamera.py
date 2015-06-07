#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
from Camera import Camera
thisCamera = Camera()
if (thisCamera.photoMode == 'motion'):
	thisCamera.motion()
if (thisCamera.photoMode == 'dark'):
	thisCamera.dark()
if (thisCamera.photoMode == 'video'):
	thisCamera.video()
if (thisCamera.photoMode == 'test'):
	thisCamera.motion()
	thisCamera.dark()
	thisCamera.video()
thisCamera.closeCam()
