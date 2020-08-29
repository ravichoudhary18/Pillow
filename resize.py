from PIL import Image

img = Image.open("image/bad_boy.jpg")
size = (450,450)
img.thumbnail(size)
img.show()
img.save("image/resize.jpg")