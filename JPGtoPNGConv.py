import os
import sys
from PIL import Image

# grab first and second argument
# to run this on command lne we need to give arguments
# python JPGtoPNGConv.py pokedex/ new/ - run in command line to run file
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new exists, and if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# loop through pokedex
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('All Done')
# convert images to png

# save to new folder
