import numpy as np


def shape_to_np(shape, dtype='int'):
    # 创建68*2用于存放坐标
    coords = np.zeros((shape.num_parts, 2), dtype=dtype)
    # 遍历每一个关键点
    # 得到坐标
    for i in range(0, shape.num_parts):
        coords[i] = (shape.part(i).x, shape.part(i).y)

    return coords


def feature_standardization(feature):
    feature -= feature[0, :]  # 以point48作为基准定位
    mean_each_col = np.average(feature, axis=0)

    # 总体方差
    variance_each_col = np.sqrt(np.sum((feature - mean_each_col) ** 2, axis=0) / feature.shape[0])
    # 样本方差
    # variance_each_col = np.sqrt(np.sum((feature - mean_each_col) ** 2,axis = 0) / (feature.shape[0] - 1))

    ret = (feature - mean_each_col) / variance_each_col
    return ret


def euclidean_distance(x, y):
    return np.sum((x - y) ** 2)


def detect_mouth_movement(imgs):
    import cv2
    import dlib

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    # 取dlib与嘴唇有关的点数（起点-终点）
    MOUSE_START = 48
    MOUSE_END = 68

    points_recorder_last, points_recorder_now = np.zeros((20, 2)), np.zeros((20, 2))

    total_count, moving_count = 0, 0
    print("检测嘴唇")
    for i in range(len(imgs)):
        if not i % 6:
            gray = cv2.cvtColor(imgs[i], cv2.COLOR_BGR2GRAY)  # 处理一帧，转为灰度图
            # 坐标为[(x1, y1) (x2, y2)]
            rets = detector(gray, 1)
            if len(rets) > 0:
                shape = predictor(gray, rets[0])
                points = shape_to_np(shape)
                mouse_points = points[MOUSE_START:MOUSE_END]

                # 使用cv2.convexHull获得位置的凸包位置
                mouseHull = cv2.convexHull(mouse_points)
                (x, y, w, h) = cv2.boundingRect(mouseHull)

                points_recorder_now = feature_standardization(mouse_points)

                sim = euclidean_distance(points_recorder_last, points_recorder_now)
                print('lip movement: ', sim)
                total_count += 1

                if sim > 0.15:
                    moving_count += 1
                    # print("lip moving...")
                # else:
                #     print("move too subtle..")

                points_recorder_last = points_recorder_now

            else:
                print("not detectable. ...", end=' ')

    print("moving_count: ", moving_count, end=' ')
    print("total_count: ", total_count)

    if total_count != 0 and moving_count / total_count >= 0.3:
        print('判断嘴唇移动')
        return True
    else:
        print('判断嘴唇未在移动')
        return False
