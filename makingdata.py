import cv2
import numpy as np

level = 2
path = "imagines/titan1.jpg"
limit = 4


def processing_data():
    def smoothing(img):
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # ret, threshold = cv2.threshold(grey, 127, 255, 0)
        thresh = cv2.Canny(grey, 150, 200)
        # cv2.imshow("a", threshold)
        thresh = cv2.dilate(thresh, None)
        thresh = cv2.erode(thresh, None)
        # cv2.imshow("b", threshold)

        return thresh

    img = cv2.imread(path)
    test = img.copy()
    threshold = smoothing(img)

    kernel_c = np.ones((5, 5), np.uint8)
    kernel_o = np.ones((1, 1), np.uint8)

    threshold = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel_c)
    threshold = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel_o)
    # cv2.imshow("c", threshold)

    edge_parameter = [(c, cv2.contourArea(c)) for c in
                      cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)[0]]
    print('Quantity of edges =  ' + str(len(edge_parameter)))

    area = set([edge[1] for edge in edge_parameter])
    area = sorted(area)
    print('List area: ' + str(area))
    distance = len(area)
    level_hard_min = area[0]
    level_hard_max = area[int(distance / 2)]
    level_normal_min = area[int(distance / 2) + 1]
    level_normal_max = area[int(distance / 2) + int(distance / 3)]
    level_easy_min = area[int(distance / 2) + int(distance / 3) + 1]
    level_easy_max = area[distance - 1]

    if level == 3:
        minn = level_hard_min
        maxx = level_hard_max
    elif level == 2:
        minn = level_normal_min
        maxx = level_normal_max
    elif level == 1:
        minn = level_easy_min
        maxx = level_easy_max

    minn = max(minn, 100)
    maxx = min(maxx, 30000)
    Limit = 6
    print("Min - Max: " + str(minn) + " " + str(maxx))
    print("Limit: " + str(Limit))

    def myFunc(e):
        return e[1]

    edge_parameter.sort(reverse=True, key=myFunc)

    for edge in edge_parameter:
        area = edge[1]
        al = np.random.randint(1, 100)
        if area <= maxx and area >= minn and al % 3 == 0:
            # x, y, w, h = cv2.boundingRect(edge[0])
            # color = img[y + h // 2, x + w // 2]

            new_color = (np.random.uniform(0, 255), np.random.uniform(0, 255), np.random.uniform(0, 255));
            cv2.fillPoly(img, [edge[0]], new_color)
            Limit = Limit - 1
            # cv2.drawContours(img, [edge[0]], 0, (0, 0, 255), 3)
            if (Limit == 0):
                break

    cv2.imwrite('output/check.jpg', threshold)
    cv2.imwrite('output/left.jpg', test)
    cv2.imwrite('output/right.jpg', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Finishing!")
