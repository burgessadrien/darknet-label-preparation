import os
import pandas as pd
import numpy as np
from PIL import Image

labels = "/home/adrien/Downloads/pothole_training/bad_road_labels/"
images = "/home/adrien/Downloads/pothole_training/bad_road_images/"
width = 0
height = 0

for filename in os.listdir(labels):
    with Image.open(images + filename.split(".")[0] + ".jpg") as img:
        width, height = img.size
    filepath = labels + filename
    file = pd.read_csv(filepath, header=None, delimiter=r" ")
    file.iloc[:,1:] = file.iloc[:,1:].astype('float64')
    for index, row in file.iterrows():
        i = 0
        tmp = 15
        while i < 4:
            temp = file.at[index, i]
            file.at[index, i] = tmp
            tmp = temp
            i +=1

        file.at[index,4] = tmp
        file.at[index, 1] = file.at[index,1] / width
        file.at[index, 2] = file.at[index,2] / height
        file.at[index, 3] = file.at[index,3] / width
        file.at[index, 4] = file.at[index,4] / height

    file.to_csv(filepath, sep=' ', float_format='%.15f', index=False, header=False)
