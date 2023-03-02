import os

import cv2
from PyQt5.QtCore import QObject, pyqtSignal, QThreadPool, QRunnable, QThread
from PyQt5.QtWidgets import QDialog

from gui import success, fail, authentication
from lip_detect import detect_mouth_movement
from record_audio import record_with_pyaudio

class Success(success.Ui_success, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_pushbutton.clicked.connect(self.close)


class Fail(fail.Ui_fail, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_pushbutton.clicked.connect(self.close)


def generate_4_digit_code():
    import random
    random_num = []
    i = 0
    while i < 4:
        num = random.randint(0, 9)
        if num == 1:  # exclude 1
            continue
        else:
            random_num.append(num)
            i += 1
    return random_num


class RecordWorker(QThread):
    finished = pyqtSignal()

    def __init__(self, filename, record_seconds):
        super().__init__()
        self.filename = filename
        self.record_seconds = record_seconds

    def run(self):
        print('开始录音')
        record_with_pyaudio(self.filename, self.record_seconds)
        print('结束录音')
        self.finished.emit()


class Authenticate(authentication.Ui_authentication, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_pushbutton.clicked.connect(self.close)
        self.start_pushbutton.clicked.connect(self.compare)
        # generate 4 digit code
        self.digit_code = generate_4_digit_code()
        # set as text
        self.num1_label.setText(str(self.digit_code[0]))
        self.num2_label.setText(str(self.digit_code[1]))
        self.num3_label.setText(str(self.digit_code[2]))
        self.num4_label.setText(str(self.digit_code[3]))

        # success or fail window
        self.success = Success()
        self.fail = Fail()

    # the core code lies here
    def compare(self):
        print('调用摄像头，按下s后开始录制视频和音频')
        cap = cv2.VideoCapture(0)

        mouth_len = 60
        imgs = []
        flag = False
        start_record = False

        while True:
            # 读取一帧图像
            ret, frame = cap.read()

            cv2.imshow('frame', frame)

            # 存储
            if flag == True:
                if start_record == False:
                    start_record = True
                    if not os.path.exists(os.path.join("records")):
                        os.makedirs(os.path.join("records"))
                    name = os.path.join("records//authenticate_audio.wav")
                    record_thread = RecordWorker(name, 4)
                    record_thread.start()

                imgs.append(frame)
                print(f"{len(imgs)}", end=' ')
                if len(imgs) == mouth_len:
                    print()
                    print('开始判断')
                    detect_mouth_movement(imgs)
                    print('判断结束')
                    break

            key = cv2.waitKey(1)

            # 按s键开始识别
            if key & 0xFF == ord('s'):
                if len(imgs) == 0 and flag == False:
                    print('开始识别')
                    flag = True

        # 释放摄像头并关闭窗口
        cap.release()
        cv2.destroyAllWindows()

        print('目前处于测试阶段，默认解锁成功')
        ans = True
        if ans:
            self.success.show()
        else:
            self.fail.show()
