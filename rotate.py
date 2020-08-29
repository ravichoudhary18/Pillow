from PIL import Image

img = Image.open("image/bad_boy.jpg")

rotate = img.rotate(45)
rotate.show()