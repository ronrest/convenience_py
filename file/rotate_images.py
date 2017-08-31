from PIL import Image

dir = "/tmp/fish/chapter4/"
rotate = 90

images = dir_items(dir, opt="files", rel=False, root="", filter="jpg")

# Rotate images
for image_file in images:
    img = Image.open(image_file)
    img = img.rotate(90)
    img.save(image_file)
