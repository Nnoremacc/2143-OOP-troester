#Name: Cameron Troester
###Date: December 6th, 2016
###Class: OOP-Progrm 3
###Description: imageEdit.py contains the bulk of the program, including functions
###that will edit a photo and return it to you

```python
from PIL import Image
import random

#given to us in class example code, even though it's highly ineffective
#so please don't blur more than 5
def blur(img,blur_power=5):
	width = img.size[0]
	height = img.size[1]
	img2 = img.copy()

	r = 0
	g = 0
	b = 0
	d = 2*blur_power * 2*blur_power
	for x in range(blur_power,width-blur_power):
		for y in range(blur_power,height-blur_power):
			for i in range(-blur_power,blur_power):
				for j in range(-blur_power,blur_power):
					pix = img.getpixel((x+i,y+j))
					r += pix[0]
					g += pix[1]
					b += pix[2]
				img2.putpixel((x,y),(int(r/d),int(g/d),int(b/d)))
			r = 0
			g = 0
			b = 0
			
	return img2

#solarize takes in a photo and compares each RGB values of the pixel
#to the level of intense that you wish (with a default of 200)
#and depending on where the color lies to the intense value, it will
#either add or subtract the intense value
def solarize(image, intense = 200):
	height = image.size[1]
	width = image.size[0]
	value = 255
	image2 = image.copy()
	for h in range(height):
		for w in range(width):
			
			pix = image.load()
				
			r, g, b = pix[w, h]
			total = (r, g, b)
			
			if r < intense:
				r = value - r
			else:
				r = r + value
			if g < intense:
				g = value - g
			else:
				g = g + value
			if b < intense:
				b = value - b
			else:
				b = b + value
				
			total = (r, g, b)
			
			image2.putpixel((w, h), (total))
	
	return image2
	
#posterize takes the image and your snap value (with a default of 64)
#it rounds each RGB value of the pixel to it's closest snap value
def posterize(image, levels = 64):

	width = image.size[0]
	height = image.size[1]
	check = levels // 2
	image2 = image.copy()
	
	for w in range(width):
		for h in range(height):
			r, g, b = image.getpixel((w, h))
			
			newred = r
			checkr = newred % levels
			
			newgreen = g
			checkg = newgreen % levels
			
			newblue = b
			checkb = newblue % levels
			
			if checkr < (check):
				newred -= checkr
			elif checkr >= (check):
				newred += (levels - checkr)
			if checkg < (check):
				newgreen -= checkg
			elif checkg >= (check):
				newgreen += (levels - checkg)
			if checkb < (check):
				newblue -= checkb
			elif checkb >= (check):
				newblue += (levels - checkb)
			total = (newred, newgreen, newblue)
			
			image2.putpixel((w, h), total)
	
	return image2

#flip will take the photo and flip it horizontally
def flip (image):
	
	width = image.size[0]
	height = image.size[1]
	image2 = image.copy()
		
	for w in range(width):
		for h in range(height // 2):
			top = image.getpixel((w, h))
			bottom = image.getpixel((w, height - 1 - h))
				
			image2.putpixel((w, height - 1 - h), top)
			image2.putpixel((w, h), bottom)
	
	return image2
	
#takes the image and changes the color of certain pixels a
#certain distance away (default set to 5) to give a glass look
def glass_effect (image, distance = 5):
		
	width = image.size[0]
	height = image.size[1]
	image2 = image.copy()

	for w in range(width):    
		for h in range(height):
			distancew = random.randint(0, distance)
			getw = w + distancew
			if getw > width -1:
				getw = w - distancew
			dish = random.randint(0, distance)
			geth = h + distancew
			if geth > height - 1:
				geth = h - distancew
			pix = image.getpixel((getw, geth))
			r = pix[0]
			g = pix[1]
			b = pix[2]
			total = (r, g, b)
			image2.putpixel((w,h), total)

	return image2
	
#with a default set to 64, this gives the photo a warhol type effect
def warhol(image, snap = 64):

	width = image.size[0]
	height = image.size[1]

	image2 = image.copy()
	
	blocks = int(255//snap)
	
	colors =[(255,0,0), (0, 255, 0), (0, 0, 255), (128, 128, 0), (0, 128, 128), (85, 85, 85)]

	for w in range(width):
		for h in range(height):

			r, g, b = image.getpixel((w, h))
			grayscale = int((r+g+b)//3)
			image2.putpixel((w, h), (grayscale, grayscale, grayscale))
			
			redo = r
			mark = redo % snap
			if mark < (snap // 2):
				redo -= mark
			else:
				redo += (snap - mark)

			for i in range(1, blocks + 1):
			   
				if redo < (i * 255) / blocks and redo > (i - 1) * 255/ blocks:
					image2.putpixel((w, h), (colors[i % 5 - 1]))
	
	return image2
```
