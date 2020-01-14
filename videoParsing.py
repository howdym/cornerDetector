import cornerDetector
from moviepy.editor import *
import cv2
import matplotlib.pyplot as plt
import cornerDetector
import numpy as np
from utils import *

cap = cv2.VideoCapture("C://Users//marcj//Desktop//01_compressed.mp4")
count = 0
page_number = 0
stop = False
while cap.isOpened():
    ret, frame = cap.read()

    if not confirm_page(frame):
        print("We are not at the page. Skipping til next photo.")
        continue

    print("We are at the selected page.")
    switch = confirm_switch(frame)

    if switch and not stop:
        print("We are going to the next page.")
        page_number += 1
        stop = True
    elif not switch and stop:
        print("We are going to the next page but we already acknowledged it.")
        stop = False
    else:
        print("This is a typical frame. No switching pages was detected.")
        # frame = cv2.resize(frame, (800, 450))
        # cv2.imshow('Frame', frame)
        # if cv2.waitKey(10000) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()

    count = count + 1

    corner, case = cornerDetector.corner_detector(filename=None, draw=True, array=frame, count=count)

# TODO: Check page count and case. Implement multiple case option; use a dictionary.

cap.release()
cv2.destroyAllWindows()  # destroy all the opened windows

# clip = VideoFileClip("C://Users//marcj//Desktop//01_compressed.mp4")
# duration = clip.duration

# for i in np.arange(0, duration + 0.2, 0.2):
  #   poi = clip.get_frame(i)

   #  stop = 0

