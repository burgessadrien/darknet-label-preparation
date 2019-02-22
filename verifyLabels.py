import os
import pandas as pd
import cv2 as cv
from PIL import Image

width = 0
height = 0

def getFileNames(source):
    fileNames = []
    for dir, subDirList, files in os.walk(source):
        for file in files:
            fileNames.append(file.split(".")[0])

    return fileNames

def displayImageLabels(imagepath, boundaries):
    img = cv.imread(imagepath, 1)
    for box in boundaries:
        cv.rectangle(img,(box[0], box[1]), (box[0] +box[2], box[1] + box[3]),(0,255,0),2)

    img = cv.resize(img, (960,540))
    cv.imshow("Display Boundaries", img)
    cv.waitKey(2000)

def getBoundaries(filepath):
    file = pd.read_csv(filepath, header=None, delimiter=" ")
    file.iloc[:,1:] = file.iloc[:,1:].astype('float64')
    boundaries = []
    for index, row in file.iterrows():
        row = []
        row.append(int(file.at[index, 1] * width))
        row.append(int(file.at[index, 2] * height))
        row.append(int(file.at[index, 3] * width))
        row.append(int(file.at[index, 4] * height))
        boundaries.append(row)

    return boundaries

if __name__ == "__main__":
    labels = "/home/adrien/Downloads/pothole_training/simple_labels/"
    images = "/home/adrien/Downloads/pothole_training/simple_images/"
    names = getFileNames(labels)

    for name in names:
        with Image.open(images + name + ".jpg") as img:
            width, height = img.size

        boundaries = getBoundaries(labels + name + ".txt")
        displayImageLabels(images + name + ".jpg", boundaries)

