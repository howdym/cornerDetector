import cornerDetector
from moviepy.editor import *
import cv2
import matplotlib.pyplot as plt
import cornerDetector
import numpy as np
import utils

cap = cv2.VideoCapture("C://Users//marcj//Desktop//01_compressed.mp4")
count = 0
while cap.isOpened():
    ret, frame = cap.read()
    plt.imshow(frame)
    if count == 0 or count > 180:
        cv2.imwrite("{}og.png".format(count), frame)
    #plt.show()
    plt.close()
    count = count + 1

    corner, case = cornerDetector.corner_detector(filename=None, draw=True, array=frame, count=count)

# TODO: look through one video. Find out how to tighten bounds to narrow down analysis.

cap.release()
cv2.destroyAllWindows()  # destroy all the opened windows

# clip = VideoFileClip("C://Users//marcj//Desktop//01_compressed.mp4")
# duration = clip.duration

# for i in np.arange(0, duration + 0.2, 0.2):
  #   poi = clip.get_frame(i)

   #  stop = 0

