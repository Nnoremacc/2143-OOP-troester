import imageEdit
from PIL import Image

	
if __name__ == "__main__":
	
	img = Image.open("flower.jpg")
	
	img2 = img.copy()
	
	img2.save('copy.jpg')
	#img = imageEdit.blur(img)
	
	#img.save('blurtest.jpg')
	
	#img = imageEdit.flip(img)
	
	#img.save('fliptest.jpg')
	
	#img = imageEdit.flip(img)
	
	#img = imageEdit.glass_effect(img)
	
	#img.save('glasstest.jpg')
	
	#img = imageEdit.posterize(img)
	
	#img.save('postertest.jpg')
	
	img = imageEdit.warhol(img)
	
	img.save('wartest.jpg')
	
	#img = imageEdit.solarize(img)
	
	#img.save('solartest.jpg')
