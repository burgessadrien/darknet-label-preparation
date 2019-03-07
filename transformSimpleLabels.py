import pandas as pd
import os
from PIL import Image
import math


labels = "/home/adrien/Downloads/pothole_training/simple_labels/"
images = "/home/adrien/Downloads/pothole_training/simple_images/"
width = 0
height = 0

for filename in os.listdir(labels):
    if filename.split(".")[1] == "txt":
        filepath = labels + filename
        try:
            with Image.open(images + filename.split(".")[0] + ".jpg") as img:
                width, height = img.size
        except:
            print("no such .jpg file: " + filename)
            continue
        file = pd.read_csv(filepath, header=None, delimiter=r" ")
        file.iloc[:,1:] = file.iloc[:,1:].astype('float64')
        data = []
        for index, row in file.iterrows():
            file.at[index, 3] = (math.ceil((file.at[index, 3] * width)) + math.ceil((file.at[index, 1] * width))) / width
            file.at[index, 4] = (math.ceil((file.at[index, 4] * height)) + math.ceil((file.at[index, 2] * height))) / height

        file.to_csv(filepath, sep=' ', float_format='%.15f', index=False, header=False)

