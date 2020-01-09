import cornerDetector
from moviepy.editor import *
import cv2
import matplotlib.pyplot as plt

# Getting sample clips
# clip = VideoFileClip("C://Users//marcj//Desktop//01_compressed.mp4")
# clip.save_frame("top.png", t="00:00:14")
# clip.save_frame("bottom.png", t="00:00:03")
# clip.save_frame("middle.png", t="00:00:28")


# Test Case 1: Top part of target image is cut off.
corner1, case1 = cornerDetector.corner_detector("top.png", False)

# Read image
img2 = cv2.imread("top.png", cv2.IMREAD_COLOR)

# Draw the corners
cv2.drawContours(img2, [corner1], 0, (0, 0, 255), 5)
for i in corner1:
    cv2.circle(img2, (i[0][0], i[0][1]), 3, 255, -1)

# Show the image
plt.imshow(img2)
plt.show()

# Check if returns right case
assert case1 == "top"


# Test Case 2: All of the image is in it.
corner2, case2 = cornerDetector.corner_detector("middle.png", False)

# Read image
img2 = cv2.imread("middle.png", cv2.IMREAD_COLOR)

# Draw the corners
cv2.drawContours(img2, [corner2], 0, (0, 0, 255), 5)
for i in corner2:
    cv2.circle(img2, (i[0][0], i[0][1]), 3, 255, -1)

# Show the image
plt.imshow(img2)
plt.show()

# Check if returns right case
assert case2 == "middle"


# Test Case 3: Bottom part of target image is cut off.
corner3, case3 = cornerDetector.corner_detector("bottom.png", False)

# Read image
img2 = cv2.imread("bottom.png", cv2.IMREAD_COLOR)

# Draw the corners
cv2.drawContours(img2, [corner3], 0, (0, 0, 255), 5)
for i in corner3:
    cv2.circle(img2, (i[0][0], i[0][1]), 3, 255, -1)

# Show the image
plt.imshow(img2)
plt.show()

# Check if returns right case
assert case3 == "bottom"
