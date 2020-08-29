from PIL import Image

size = (450,450)
img = Image.new("RGB",size,"red")
img.show()
img.save("image/blank.jpg")