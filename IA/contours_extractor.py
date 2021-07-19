import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import rcParams
import numpy as np
import sys
import cv2
from optparse import OptionParser
import json
from json import *
import time
import os 
from numpyencoder import NumpyEncoder

parser = OptionParser()
parser.add_option("-i", "--input", dest="input_filename", help="image file path")
parser.add_option("-o", "--output", dest="output_filename", help="output file path")
(options, args) = parser.parse_args()

if not options.input_filename:
    raise ValueError("Invalid image filepath")
    exit()
else: 
    print("Script status : input path validate")
    time.sleep(0.6)

if not options.output_filename:
    raise ValueError("Invalid output filepath - " + options.output_filename)
    exit()
else: 
    print("Script status : output path validate")
    time.sleep(0.6)

input_filename = options.input_filename
output_filename = options.output_filename
# filename = os.path.basename(image_filename)

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


for filename in os.listdir(input_filename):
    if filename.endswith(".png") or filename.endswith(".jpg"):

        print(filename)
        if filename.endswith(".png"):
            filename_clear = filename.replace(".png", ".json")
        elif filename.endswith(".jpg"):
            filename_clear = filename.replace(".jpg", ".json")

        img = cv2.imread(input_filename + "/" + filename)
        color = (255, 0, 0)
        imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 127, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        canvas = np.zeros_like(img)
        result = cv2.drawContours(canvas, contours, 0, color, 2, cv2.LINE_8, hierarchy, 2)

        data = {"filename": filename, "contours" : result.tolist()}
        with open(output_filename + "/" + filename_clear, "w") as out_f:
            json.dump(data, out_f)








# data = {"contours": result, "filename": str(filename)}

# with open(output_filename, "w") as out_f:
#     json.dump(data, out_f, cls=NumpyArrayEncoder)