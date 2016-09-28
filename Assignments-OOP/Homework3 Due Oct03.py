"""
Name: Cameron Troester
Email: cdtroester1022@my.mwsu.edu
Assignment: Homework 3 - Simple Shift Cipher
Due: 03 October @ 1:00 p.m
"""


"""
@ Name: ShiftCipher
@ Description: Simple class to do a shift cipher that will remove any non letters/numbers
"""

class ShiftCipher(object):
	
	
	"""
	@ Name: __init__
	@ Description: the constructor of the class containing all variables needed
	@ Params:
	     None
	"""
	def __init__(self):
		
		self.plainText = None
		self.cipherText = None 
		self.cleanText = None 
		self.shift = 3
		self.numbers = ['0','1','2','3','4','5','6','7','8','9']
		self.alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		self.smallalpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		
	
	"""
	@ Name: __str__
	@ Description: Prints out all the data we need
	@ Params:
	     None
	"""
	def __str__(self):
		return "plainText: %s\ncipherText: %s\ncleanText: %s\nshift: %d\n" % (self.plainText,self.cipherText,self.cleanText,self.shift)
		
	
	"""
	@ Name: promptUserMessage
	@ Description: this will take in the keyboard input as the message to be used for the encryption
	@ Params:
	     None
	"""
	def promptUserMessage(self):
		temp = input("Message: ")
		self.setMessage(temp)
		
		
	"""
	@ Name: setMessage
	@ Description: will either encrypt or decrypt the message given depending on which one is needed
	@ Params:
	     message (String) -- variable that holds the message that was inputted
	     encrypted (bool) -- default set to False, checks to see if the message is already encrypted or not
	"""
	def setMessage(self,message,encrypted = False):
		if(not encrypted):
			self.plainText = message
			self.cleanData()
			self.__encrypt()
		else:
			self.plainText = message
			self.cipherText = message
			self.__decrypt()
			
			
	"""
	@ Name: getCipherText
	@ Description: a getter that will just return the encrypted message as a string
	@ Params:
	     None
	"""
	def getCipherText(self):
		return self.cipherText
	
	
	"""
	@ Name: getPlainText
	@ Description: getter that will return the normal message that the user either inputted or viewed
	@ Params:
	     None
	"""
	def getPlainText(self):
		return self.plainText
	
	
	"""
	@ Name: setShirt
	@ Description: a setter that will change how large you want to shift by
	@ Params:
	     None
	"""
	def setShift(self,shift):
		self.shift = shift
		
		
	"""
	@ Name: getShift
	@ Description: a getter that will return the value that you shifted by
	@ Params:
	     None
	"""	
	def getShift(self):
		return self.shift
	
	
	"""
	@ Name: cleanData
	@ Description: it will run through the string that is the message, removing all unneeded character values such as special characters and spaces. Also turning all letters to uppercase
	@ Params:
	     None
	"""
	def cleanData(self):
		self.cleanText = ''
		for letter in self.plainText:
			if letter in self.smallalpha:
				self.cleanText += chr(ord(letter) - 32)
			
			if letter in self.numbers:
				self.cleanText += letter
				
			if letter in self.alpha:
				self.cleanText += letter
				
			else:
				continue
			
			
	"""
	@ Name: __encrypt
	@ Description: private method that will change the text to it's new encrypted and hard to read message
	@ Params:
	     None
	"""
	def __encrypt(self):
		self.cipherText = ''
		if(not self.cleanText):
			return
		for letter in self.cleanText:
			if letter in self.alpha:
				self.cipherText += chr(((ord(letter) - 65 + self.shift) % 26) + 65)
				
			if letter in self.numbers:
				self.cipherText += chr(((ord(letter) - 48 + self.shift) % 10) + 48)
			
	
	"""
	@ Name: __decrypt
	@ Description: private method that will take the encrypted message and change it back into normal language
	@ Params:
	     None
	"""
	def __decrypt(self):
		self.cleanText= ''
		if(not self.cipherText):
			return
		for letter in self.cipherText:
			if letter in self.alpha:
				self.cleanText += chr(((ord(letter) - 65 - self.shift) % 26) + 65)
				
			if letter in self.numbers:
				self.cleanText += chr(((ord(letter) - 48 - self.shift) % 10) + 48)
		
		
alice = ShiftCipher()
alice.promptUserMessage()
print("Alice's: ")
print(alice)

bob = ShiftCipher()
bob.setMessage(alice.getCipherText(),True)
print("Bob's: ")
print(bob)
