from PIL import Image

img=Image.open("ppp.jpg")
new_img=img.convert("L")			#black & white
new_img.show()

new_img1=img.convert("CMYK")
new_img1.show()
