import os
import pandas as pd
import numpy as np
from PIL import Image

labels = "/home/adrien/Downloads/test_pothole/labels/"
images = "/home/adrien/Downloads/test_pothole/images/"
width = 0
height = 0

for filename in os.listdir(labels):
    with Image.open(images + filename.split(".")[0] + ".jpg") as img:
        width, height = img.size
    filepath = labels + filename
    file = pd.read_csv(filepath, header=None, delimiter=r" ")
    file.iloc[:,1:] = file.iloc[:,1:].astype('float64')
    data = []
    for index, row in file.iterrows():
        data.append([15, file.at[index, 0] / width, file.at[index,1] / height, file.at[index, 2] / width, file.at[index,3] / height])
    data = np.array(data)
    print(width)
    print(height)
    np.savetxt(filepath, data, delimiter=" ", fmt='%f')
