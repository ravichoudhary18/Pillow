from PIL import Image

img = Image.open("image/bad_boy.jpg")
print(img.width)
print(img.height)
print(img.mode)
print(img.size)
print(img.format)
img.show()