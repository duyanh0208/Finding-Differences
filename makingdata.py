import cv2
import numpy as np




def processing_data(path, level, limit):
    def smoothing(img):
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.Canny(grey, 150, 200)
        thresh = cv2.dilate(thresh, None)
        thresh = cv2.erode(thresh, None)

        return thresh

    img = cv2.imread(path)
    test = img.copy()

    threshold = smoothing(img)

    edge_parameter = [(c, cv2.contourArea(c)) for c in
                      cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)[0]]

    area = set([edge[1] for edge in edge_parameter])
    area = sorted(area)

    distance = len(area)

    if level == 3:
        minn = area[0]
        maxx = area[int(distance / 2)]

    if level == 2:
        minn = area[int(distance / 2) + 1]
        maxx = area[int(distance / 2) + int(distance / 3)]

    if level == 1:
        minn = area[int(distance / 2) + int(distance / 3) + 1]
        maxx = area[distance - 1]


    Limit = 6

    def myFunc(e):
        return e[1]

    edge_parameter.sort(reverse=True, key=myFunc)

    for edge in edge_parameter:
        area = edge[1]
        al = np.random.randint(1, 100)
        if area <= maxx and area >= minn and al % 3 == 0:
            new_color = (np.random.uniform(0, 255), np.random.uniform(0, 255), np.random.uniform(0, 255));
            cv2.fillPoly(img, [edge[0]], new_color)
            Limit = Limit - 1
            if (Limit == 0):
                break

    cv2.imwrite("output/left_" + str(level) + ".jpg", test)
    cv2.imwrite("output/right_" + str(level) + ".jpg", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
