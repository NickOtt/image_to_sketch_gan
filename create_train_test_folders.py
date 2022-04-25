import glob
import os
import random
import shutil
import re

PATH = 'data/sketch_and_images/'
PHOTO = 'photo/tx_000000000000/'
TRAIN = 'single_cat/train/'
SKETCH = 'sketch/tx_000000000000/'
VAL = 'single_cat/val/'

folder_list = []
directory_list = os.listdir(PATH + PHOTO)

# Copy files to training directory
#for folder in directory_list[0]:
folder = directory_list[0] + "/"

for img_name in glob.glob(PATH + PHOTO + folder + '*.jpg'):
    shutil.copy(img_name, PATH + TRAIN)
print("Moved {} photos".format(folder))

for img_name in glob.glob(PATH + SKETCH + folder + '*-1.png'):
    shutil.copy(img_name, PATH + TRAIN)
print("Moved {} sketches".format(folder))

# Move % of files from training to validation set
# for n in range(1000):
#     rand_file = random.choice(os.listdir(PATH+TRAIN))
    
#     source_file = "%s%s"%(PATH+TRAIN, rand_file)
#     shutil.move(source_file, PATH+VAL)
    
#     if rand_file.endswith(".jpg"):
#         shutil.move(source_file.replace('.jpg', '-1.png'), PATH+VAL)
#     else:
#         shutil.move(source_file.replace('-1.png', '.jpg'), PATH+VAL)