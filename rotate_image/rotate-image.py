from PIL import Image

im = Image.open("piza.jpg")

# im.rotate(45).show()

im = im.rotate(45)

im.save("piza2.jpg")

im.show()
