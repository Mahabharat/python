from PIL import Image

img1=Image.open("paul.jpg")
img2=Image.open("cocal.jpg")


print(img1.size)
print(img2.size)

area=(100,100,222,308)
img1.paste(img2, area)
img1.show()
