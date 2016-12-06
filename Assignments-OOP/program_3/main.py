#Name: Cameron Troester
#Date: December 6th, 2016
#Class: OOP-Progrm 3
#Description: main.py is where I grab the photo and run the many functions on it


import imageEdit
from PIL import Image
import sys

	
#Main function that will ask the user for a filename
#attempt to load the file, and then run all functions on 
#copies of the photo, so each one is independent.
if __name__ == "__main__":
	
	filename = input("Name of file you want to open: ")
	
	try:
		img = Image.open(filename)
	except:
		print("Could not find filename, exiting")
		sys.exit()
	
	img2 = img.copy()
	img3 = img.copy()
	img4 = img.copy()
	img5 = img.copy()
	img6 = img.copy()
	
	img2.save('copy.jpg')
	
	img = imageEdit.blur(img)
	
	img.save('blurtest.jpg')
	
	img2 = imageEdit.flip(img2)
	
	img2.save('fliptest.jpg')
	
	img3 = imageEdit.glass_effect(img3)
	
	img3.save('glasstest.jpg')
	
	img4 = imageEdit.posterize(img4)
	
	img4.save('postertest.jpg')
	
	img5 = imageEdit.warhol(img5)
	
	img5.save('wartest.jpg')
	
	img6 = imageEdit.solarize(img6)
	
	img6.save('solartest.jpg')
