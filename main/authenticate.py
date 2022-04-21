from PyQt5.QtWidgets import QDialog

from gui import success, fail, authentication


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


# filename could be absolute path
def record_with_pyaudio(filename, record_seconds=10, fs=16000):
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for record seconds
    for i in range(0, int(fs / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()


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

    def compare(self):
        # the core code
        ans = True

        if ans == True:
            self.success.show()
        else:
            self.fail.show()
