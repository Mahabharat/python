from PIL import Image

img=Image.open("om.jpg")
print(img.size)
print(img.format)
'''
area=(184,160,284,360)			#top left, bottom right
cropped_img=img.crop(area)

img.show()
cropped_img.show()
'''
