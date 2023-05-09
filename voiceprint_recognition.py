import sys

from PyQt5.QtWidgets import QApplication

import main.interface

if __name__ == "__main__":
    import sys
    sys.path.append('./speech_recognition')
    sys.path.append('./voice_recognition')

    app = QApplication(sys.argv)

    window = main.interface.MainWindow()
    window.initial.show()

    sys.exit(app.exec())
