import os
class MySet:
	def __init__(self):
		self.names = ['photoMode','waitStart','waitTime','waitEnd','cameraResolution','noImages','sessionTime','shutDownWhenDone','ledOn','cameraMode','detectLimit','shutterSpeed','recordingTime','noFiles']
		self.values = ['motion','3','0','0','mid','100','60','True','True','auto','3','1','10','1']
	def writeToFile(self):
		f = open('settings.txt','w')
		index = 0
		for name in self.names:
			value = self.values[index]
			index = index + 1
			f.write(name+'='+value+'\n')
	def writeToConsole(self):
		print '*****CURRENT SETTINGS******'
		index = 0
		for name in self.names:
			value = self.values[index]
			index = index + 1
			print(name+'='+value)
		print '**************************'
	def startMenu(self):
		while True:
			x.writeToConsole()
			print 'OPTIONS:'
			print '(e) Edit'
			print '(s) Save'
			print '(x) Exit'
			uInput = raw_input('>> ')
			if uInput != 'e' and uInput != 's' and uInput != 'x':
				print '\nWRONG INPUT!!!!\n'
				continue
			return uInput
	def editMenu(self):
		print 'EDIT:'	
		self.setInt(1)
		self.setInt(2)
		#self.setInt(3)
		self.setOption(4,['low','mid','high']);
		self.setInt(5)
		self.setInt(6)
		#self.setOption(7,['True','False']);
		self.setOption(8,['True','False']);
		self.setInt(10)
	def setInt(self,index):
		try:
			newValue = int(raw_input(self.names[index]+' >> '))
			self.values[index] = str(newValue)
		except :
			print "Oops!  That was no valid number.  Try again..."	
	def setOption(self,index,options):
		while True:
			for x in range(0,len(options)):
				print '  ('+str(x)+') '+options[x]
			newValue = raw_input(self.names[index]+' >> ')
			isCorrect = 0
			for x in range(0,len(options)):
				if newValue == str(x):
					isCorrect = 1
					self.values[index] = options[x]
					return
			if isCorrect == 0:
				print "Oops!  That was no valid number.  Try again..."
	def saveMenu(self):
		self.writeToFile()
		print 'file saved in folder: '+os.getcwd()+' as settings.txt'
			
""" main """
x = MySet()
while True:
	userInputMain =x.startMenu()
	if userInputMain == 'e':
		x.editMenu()
	if userInputMain == 's':
		x.saveMenu()
		break
	if userInputMain == 'x':
		break
