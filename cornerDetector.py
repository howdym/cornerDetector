import cv2
import numpy as np
from matplotlib import pyplot as plt


def corner_detector(filename, draw=True, array=None, count=0):

    if array is None:
        # Reading image
        img2 = cv2.imread(filename, cv2.IMREAD_COLOR)

        # Reading same image in another variable and
        # converting to gray scale.
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    else:
        img2 = array

        img = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

    # Converting image to a binary image
    # (black and white only image).
    _, threshold = cv2.threshold(img, 110, 255,
                                 cv2.THRESH_BINARY)

    # Cut top and bottom
    threshold[677:720, 0:1280] = 0
    threshold[0:73, 0:1280] = 0

    # plt.figure()
    # plt.imshow(threshold)
    # plt.show()
    # plt.close()

    # Detecting shapes in image by selecting region
    # with same colors or intensity.
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE,
                                   cv2.CHAIN_APPROX_SIMPLE)

    targets = []
    case = ""

    # Searching through every region selected to
    # find the required polygon.
    for cnt in contours:
        area = cv2.contourArea(cnt)

        # Shortlisting the regions based on there area.
        if area > (44000 + 40 * 1280) and area < 1280 * 593:
            approx = cv2.approxPolyDP(cnt,
                                      0.009 * cv2.arcLength(cnt, True), True)

            # Approx is the coordinates of the corners.

            # Checking if the no. of sides of the selected region is 4.
            if len(approx) == 4:
                targets = approx
                case = "middle"
            elif len(approx) == 8:
                temp = []
                for i in approx:
                    temp.append(i[0][0])
                temp = np.argsort(temp)
                temp = np.delete(temp, [0, 1, 6, 7])
                approx = approx[temp]

                #
                for i in approx:
                    if i[0][1] == 73:
                        case = "top"
                        break
                    else:
                        case = "bottom"
                targets = approx

            # Checking if image wants to be drawn
            if draw and (len(approx) == 4 or len(approx) == 8):
                cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5)
                for i in approx:
                    cv2.circle(img2, (i[0][0], i[0][1]), 3, 255, -1)

    # Showing the image along with outlined box.
    img2 = cv2.resize(img2, (800, 450))
    cv2.imshow('Frame', img2)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

    return targets, case
