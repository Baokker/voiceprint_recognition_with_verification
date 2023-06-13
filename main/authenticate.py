import os

import cv2
from PyQt5.QtCore import QObject, pyqtSignal, QThreadPool, QRunnable, QThread
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic.properties import QtWidgets

from gui import success, fail, authentication

from lip_detect import detect_mouth_movement

from speech_recognition.CNN_use import predict_4_digit_audio

from record_audio import record_with_pyaudio

from voice_recognition.infer_recognition import recognize


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


class CheckResult:
    def __init__(self):
        self.voice_flag = False
        self.speech_flag = False
        self.lip_flag = False

    def set_voice_flag(self, bool):
        self.voice_flag = bool

    def set_lip_flag(self, bool):
        self.lip_flag = bool

    def set_speech_flag(self, bool):
        self.speech_flag = bool

    def check_func(self):
        return self.voice_flag and (self.speech_flag or self.lip_flag)


check_result = CheckResult()


def generate_4_digit_code():
    import random
    random_num = []
    i = 0
    while i < 4:
        num = random.randint(0, 9)
        if num in random_num:
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


class VoiceRecognizer(QThread):
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        print('开始识别声纹')
        result = recognize()
        check_result.set_voice_flag(result)
        print('结束识别声纹')
        self.finished.emit()


def judge_chinese_num_accuracy(origin_arr, result_arr):
    print('origin array:', origin_arr)
    print('result array:', result_arr)

    count = 0

    min_len = min(len(origin_arr), len(result_arr))

    for i in range(min_len):
        if origin_arr[i] == result_arr[i]:
            count += 1

        if count / 4 >= 3 / 4:
            return True

    return False


class SpeechRecognizer(QThread):
    finished = pyqtSignal()

    def __init__(self, origin_arr):
        super().__init__()
        self.origin_arr = origin_arr

    def run(self):
        print('开始识别语音')
        result = predict_4_digit_audio()
        check_result.set_speech_flag(judge_chinese_num_accuracy(self.origin_arr, result))
        print('结束识别语音')
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

    def check_result_func(self):
        if self.voice_recognizer.isRunning() or self.speech_recognizer.isRunning():
            return
        # 以下是检查结果的代码
        ans = check_result.check_func()
        if ans:
            self.success.show()
        else:
            self.fail.show()

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

                    record_time = 5
                    self.record_thread = RecordWorker(name, record_time)
                    self.record_thread.start()

                    # 等待一段时间，让 record_thread 有足够的时间启动并运行
                    QThread.msleep(100)

                    self.voice_recognizer = VoiceRecognizer()
                    self.speech_recognizer = SpeechRecognizer(self.digit_code)
                    self.record_thread.finished.connect(self.voice_recognizer.start)
                    self.record_thread.finished.connect(self.speech_recognizer.start)

                    self.voice_recognizer.finished.connect(self.check_result_func)
                    self.speech_recognizer.finished.connect(self.check_result_func)

                    # 启动事件循环
                    QApplication.processEvents()

                imgs.append(frame)
                print(f"{len(imgs)}", end=' ')

                if len(imgs) % 10 == 0:
                    print()

                if len(imgs) == mouth_len:
                    print()
                    print('开始判断嘴唇')
                    result = detect_mouth_movement(imgs)
                    check_result.set_lip_flag(result)
                    print('嘴唇判断结束')
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
