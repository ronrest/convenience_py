"""Rotate all the images in a given directory"""
from PIL import Image
import glob
import os

dir = "/tmp/"
ext = ".jpg" # It should include the "."
rotate = 90

# Rotate images
images = glob.glob(os.path.join(dir, "*"+ext))
for image_file in images:
    img = Image.open(image_file)
    img = img.rotate(90)
    img.save(image_file)
