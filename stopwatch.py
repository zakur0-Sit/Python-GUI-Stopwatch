import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()

        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Stopwatch")

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addWidget(self.time_label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.start_button.setObjectName("start_button")
        self.stop_button.setObjectName("stop_button")
        self.reset_button.setObjectName("reset_button")

        self.setStyleSheet("""
            QPushButton
            {
                font-size: 20px;
                padding: 10px 50px;
                margin: 0 5px;
                color: #fff;
                border: none;
                cursor: pointer;
            }
            
            QLabel
            {
                font-size: 50px;
                padding: 30px 40px;
                background-color: #1E2021;
                color: cornflowerblue;
            }
            
            #start_button
            {
                background-color: lightgreen;
            }
            
            #stop_button
            {
                background-color: tomato;
            }
            
            #reset_button
            {
                background-color: cornflowerblue;
            }
        """)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText((self.format_time(self.time)))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stop_watch = StopWatch()
    stop_watch.show()
    sys.exit(app.exec_())