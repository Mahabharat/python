from PIL import Image
img=Image.open("jay.jpg")
img1=Image.open("om.jpg")

r1,g1,b1=img.split()
r2,g2,b2=img1.split()

new_img=Image.merge("RGB",(r1,b1,g1))
new_img.show()

new_img1=Image.merge("RGB",(r2,b2,g2))
new_img1.show()

new_img1=Image.merge("RGB",(r2,b1,g2))		#size should be same
new_img1.show()


