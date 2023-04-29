# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂
from pathlib import Path

from PIL import Image

# creating paths
ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.jpg'
NEW_IMAGE = ROOT_FOLDER / 'new.jpg'

# open image
pil_image = Image.open(ORIGINAL)
# get image size
width, height = pil_image.size
# get info of image
exif = pil_image.info['exif']

# calculating new width and height
# width     new_width
# height    ??
new_width = 640
new_height = round(height * new_width / width)
print(new_width, new_height)

# resizing image
new_image = pil_image.resize((new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
    exif=exif
)
