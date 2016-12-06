from PIL import Image
import random
	
#given to us in class example code, even though it's highly ineffective
#so please don't blur more than 5
def blur(img,blur_power=5):
	width = img.size[0]
	height = img.size[1]

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
				img.putpixel((x,y),(int(r/d),int(g/d),int(b/d)))
			r = 0
			g = 0
			b = 0
			
	return img

def solarize(image, intense = 200):
	height = image.size[1]
	width = image.size[0]
	value = 255
		
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
			
			image.putpixel((w, h), (total))
			
	return image
	
def posterize(image, levels = 64):

	width = image.size[0]
	height = image.size[1]
	check = levels // 2
	
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
			
			image.putpixel((w, h), total)
			
	return image

def flip (image):
	
	width = image.size[0]
	height = image.size[1]
		
	for w in range(width):
		for h in range(height // 2):
			top = image.getpixel((w, h))
			bottom = image.getpixel((w, height - 1 - h))
				
			image.putpixel((w, height - 1 - h), top)
			image.putpixel((w, h), bottom)
				
	return image
	
def glass_effect (image, distance = 5):
		
	width = image.size[0]
	height = image.size[1]

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
			image.putpixel((w,h), total)

	return image
	
def warhol(image, snap = 64):

	width = image.size[0]
	height = image.size[1]

	
	blocks = int(255//snap)
	
	colors =[(255,0,0), (0, 255, 0), (0, 0, 255), (128, 128, 0), (0, 128, 128), (85, 85, 85)]

	for w in range(width):
		for h in range(height):

			r, g, b = image.getpixel((w, h))
			grayscale = int((r+g+b)//3)
			image.putpixel((w, h), (grayscale, grayscale, grayscale))
			
			redo = r
			mark = redo % snap
			if mark < (snap // 2):
				redo -= mark
			else:
				redo += (snap - mark)

			for i in range(1, blocks + 1):
			   
				if redo < (i * 255) / blocks and redo > (i - 1) * 255/ blocks:
					image.putpixel((w, h), (colors[i % 5 - 1]))
					
	return image
