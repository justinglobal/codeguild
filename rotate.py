from PIL import Image

im = Image.open("piza.jpg")

im.rotate(45).show()


