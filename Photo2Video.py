#!/usr/bin/env python3

"""Склеиватель фоток в видео

Этот скрипт собирает видео из фотографий.

Пример запуска:
    Photo2Video.py c:\dir
"""

import sys
import os
import cv2 # $ pip install opencv-python
WorkDir = sys.argv[1]
files =  os.listdir(WorkDir)
frames = []
for i in files:
    frames.append(os.path.join (WorkDir, i))
frame = cv2.imread(frames[0]) # get size from the 1st frame 
writer = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10.0, (frame.shape[1], frame.shape[0]), isColor=len(frame.shape) > 2)
for frame in map(cv2.imread, frames):
    writer.write(frame)
writer.release()
cv2.destroyAllWindows()