import os
import sys
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#print(image_folder, output_folder)
# check if new exists, and if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# loop through pokedex

# convert images to png

# save to new folder
