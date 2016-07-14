from PIL import Image
img=Image.open("ppp.jpg")
img.show()

new_img=img.resize((50,50))
new_img.show()

new_img1=img.transpose(Image.ROTATE_90)
new_img1.show()

new_img2=img.transpose(Image.FLIP_TOP_BOTTOM)
new_img2.show()

