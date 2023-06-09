import cv2
import imutils
import numpy as np


def Thresh_Dilated(dissimilar):
    dissimilar = cv2.cvtColor(dissimilar, cv2.COLOR_BGR2GRAY)

    for i in range(0, 3):
        dilated = cv2.dilate(dissimilar.copy(), None, iterations=i + 1)
    (T, thresh) = cv2.threshold(dilated, 3, 255, cv2.THRESH_BINARY)

    kernel = np.ones((3, 3), np.uint8)
    dilate = cv2.dilate(thresh, kernel, iterations=5)
    return dilate


def spotting(level):
    image1 = cv2.imread("output/left_"+ str(level) + ".jpg")
    image2 = cv2.imread("output/right_"+ str(level) + ".jpg")
    image1 = imutils.resize(image1, height=460)
    image2 = imutils.resize(image2, height=460)

    img_height = image1.shape[0]

    dissimilar = cv2.absdiff(image1, image2)

    dilate = Thresh_Dilated(dissimilar)

    edges = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    edges = imutils.grab_contours(edges)
    cnt = 0
    for edge in edges:
        if cv2.contourArea(edge) >= 60:
            cnt += 1
            x, y, w, h = cv2.boundingRect(edge)
            cv2.rectangle(image1, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(image2, (x, y), (x + w, y + h), (0, 0, 255), 2)

    x = np.zeros((img_height, 10, 3), np.uint8)
    outcome = np.hstack((image1, x, image2))
    cv2.imshow("Showing differences", outcome)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
