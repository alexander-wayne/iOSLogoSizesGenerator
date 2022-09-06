# Made by Alex Wayne on 09/06/22

from PIL import Image


originalFile = "logo.png"

originalImage = Image.open(originalFile)

sizes = [180, 167, 152, 120, 87, 80, 76, 60, 58, 40, 29, 20]

for size in sizes:
    sizedImage = originalImage.resize((size, size))
    sizedImage.save("logo_%d.png" % size)
