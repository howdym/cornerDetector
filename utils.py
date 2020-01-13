import cv2
import numpy as np
import matplotlib.pyplot as plt


def template_helper(img, target):
    h = target.shape[0]
    w = target.shape[1]

    res = cv2.matchTemplate(img[:, :, 0], target[:, :, 0], cv2.TM_SQDIFF_NORMED)
    res += cv2.matchTemplate(img[:, :, 1], target[:, :, 1], cv2.TM_SQDIFF_NORMED)
    res += cv2.matchTemplate(img[:, :, 2], target[:, :, 2], cv2.TM_SQDIFF_NORMED)
    threshold = 0.001
    loc = np.where(res <= threshold)
    img_rgb = img.copy()

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    plt.imshow(img_rgb)
    #plt.show()
    plt.close()

    return len(loc[0]) == 1 and len(loc[1]) == 1


# Find out if person is on the page of interest
def confirm_page(img):
    img2 = cv2.imread("bottom.png")
    target = img2[680:720, 590:638, :]
    return template_helper(img, target)


# Find out if person is on the page of interest
def confirm_switch(img):
    img2 = cv2.imread("moving.png")
    target = img2[546:580, 941:997, :]
    return template_helper(img, target)
