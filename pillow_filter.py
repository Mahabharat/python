from PIL import Image
from PIL import ImageFilter

img=Image.open("ppp.jpg")
img.show()

blur=img.filter(ImageFilter.BLUR)
detail=img.filter(ImageFilter.DETAIL)
find=img.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
find.show()
