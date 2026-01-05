# pickle convert routine from Jiggly-Balls/nightshade-release

from PIL import Image
import numpy as np
import os


image_data = data['img']

plt.imshow(image_data)
txt_data = data['text']
directory = "C:\\Users\\saffr\\OneDrive - Nanyang Technological University\\NTU\\Y4 FYP\\fyp_nightshade\\dataset"
img_filename = f"{txt_data}.jpg"
img_path = os.path.join(directory, img_filename)
img_jpg = Image.fromarray(np.uint8(image_data))
img_jpg.save(img_path)\
txt_filename = f"{txt_data}.txt"
txt_path = os.path.join(directory, txt_filename)
with open(txt_path, 'w') as txt_file:
    txt_file.write(txt_data)
