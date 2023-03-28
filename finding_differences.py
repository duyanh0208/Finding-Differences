import cv2
import imutils
import numpy as np


def spotting():
    imagine1 = cv2.imread("output/Left.jpg")
    imagine2 = cv2.imread("output/Right.jpg")
    # blur_image = cv2.blur(imagine1, (5, 5))
    # cv2.imshow('Blurred Image', blur_image)
    imagine1 = imutils.resize(imagine1, height=460)
    imagine2 = imutils.resize(imagine2, height=460)

    img_height = imagine1.shape[0]

    dissimilar = cv2.absdiff(imagine1, imagine2)
    cv2.imshow("Dissimilar", dissimilar)

    dissimilar = cv2.cvtColor(dissimilar, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Grey dissimilar", dissimilar)
    for i in range(0, 3):
        dilated = cv2.dilate(dissimilar.copy(), None, iterations=i + 1)
    (T, thresh) = cv2.threshold(dilated, 3, 255, cv2.THRESH_BINARY)

    kernel = np.ones((3, 3), np.uint8)
    dilate = cv2.dilate(thresh, kernel, iterations=5)
    cv2.imshow("Dilate", dilate)

    edges = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    edges = imutils.grab_contours(edges)
    cnt = 0
    for edge in edges:
        if cv2.contourArea(edge) >= 60:
            cnt = cnt + 1
            x, y, w, h = cv2.boundingRect(edge)
            cv2.rectangle(imagine1, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(imagine2, (x, y), (x + w, y + h), (0, 0, 255), 2)

    x = np.zeros((img_height, 10, 3), np.uint8)
    outcome = np.hstack((imagine1, x, imagine2))
    print("Quantity of differences:", str(cnt))
    cv2.imshow("Differences", outcome)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
