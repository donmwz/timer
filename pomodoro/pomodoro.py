import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QMessageBox
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
import pygame
from datetime import datetime
import time

class Timer(QWidget):
    message_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pomodoro")
        self.setStyleSheet("background-color: #1A1A1A;")
        self.layout = QVBoxLayout(self)
        self.setWindowIcon(QIcon('images.png')) 

        self.create_widgets()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.counter = 0

        self.timer_pomodoro = QTimer(self)
        self.timer_pomodoro.timeout.connect(self.update_label_pomodoro)
        self.counter_pomodoro = 0
    
        self.message_signal.connect(self.show_message)


    def create_widgets(self):

        self.settings_btn = QPushButton(self, text="S")
        self.settings_btn.clicked.connect(self.settings)
        self.settings_btn.setGeometry(20, 20 ,40, 40)
        self.settings_btn.setStyleSheet("""
            QPushButton {
                background-color: purple;
                color: white;
                border-radius: 20px;
                border: none;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: blue;
            }
        """)

        self.settings_hide_btn = QPushButton(self, text="S")
        self.settings_hide_btn.clicked.connect(self.settings_hide)
        self.settings_hide_btn.setGeometry(20, 20 ,40, 40)
        self.settings_hide_btn.setStyleSheet("""
            QPushButton {
                background-color: purple;
                color: white;
                border-radius: 20px;
                border: none;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: blue;
            }
        """)
        self.settings_hide_btn.hide()

        self.mini_mode_btn = QPushButton(self, text="M")
        self.mini_mode_btn.clicked.connect(self.settings)
        self.mini_mode_btn.setDisabled(True)
        self.mini_mode_btn.setGeometry(220, 20 ,40, 40)
        self.mini_mode_btn.setStyleSheet("""
            QPushButton {
                background-color: blue;
                color: white;
                border-radius: 20px;
                border: none;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: darkblue;
            }
        """)
        self.mini_mode_btn.hide()

        self.light_btn = QPushButton(self, text="L")
        self.light_btn.setGeometry(70, 20 ,40, 40)
        self.light_btn.clicked.connect(self.light)
        self.light_btn.setObjectName('light_btn')
        self.light_btn.setStyleSheet("""
            QPushButton {
                background-color: orange;
                color: white;
                border-radius: 20px;
                border: none;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: white;
                color: black;
            }
        """)
        self.light_btn.hide()

        self.dark_btn = QPushButton(self, text="D")
        self.dark_btn.setGeometry(120, 20 ,40, 40)
        self.dark_btn.setObjectName('light_btn')
        self.dark_btn.clicked.connect(self.dark)
        self.dark_btn.setStyleSheet("""
            QPushButton {
                background-color: gray;
                color: white;
                border-radius: 20px;
                border: none;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: black;
            }
        """)
        self.dark_btn.hide()

        self.langue_e_btn = QPushButton(self, text="E")
        self.langue_e_btn.setGeometry(170, 20 ,40, 40)
        self.langue_e_btn.clicked.connect(self.langue_e)
        self.langue_e_btn.setObjectName('light_btn')
        self.langue_e_btn.setStyleSheet("""
            QPushButton {
                background-color: #FF6347;
                color: white;
                border-radius: 20px;
                border: none;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: red;
            }
        """)
        self.langue_e_btn.hide()

        self.langue_a_btn = QPushButton(self, text="أ")
        self.langue_a_btn.setGeometry(221, 20 ,40, 40)
        self.langue_a_btn.clicked.connect(self.langue_a)
        self.langue_a_btn.setObjectName('light_btn')
        self.langue_a_btn.setStyleSheet("""
            QPushButton {
                background-color: green;
                color: white;
                border-radius: 20px;
                border: none;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: darkgreen;
            }
        """)
        self.langue_a_btn.hide()

        self.main_btn = QPushButton(self, text="")
        self.main_btn.setGeometry(630, 300, 650, 430)
        self.main_btn.setDisabled(True)
        self.main_btn.setStyleSheet("""
            QPushButton {
                background-color: #222222;
                font-size: 100px;
                color: white;
            }
        """)

        self.timer_btn = QPushButton(self, text="Zaman")
        self.timer_btn.setGeometry(710, 330, 150, 50)
        self.timer_btn.clicked.connect(self.timer)
        self.timer_btn.setStyleSheet("""
            QPushButton {
                background-color: #222222;
                color: #F0F0F0;
                font: 17px;
                border: none;
            }
            QPushButton:hover {
                background-color: #242424;
            }
        """)

        self.stopwatch_btn = QPushButton(self, text="Kronometre")
        self.stopwatch_btn.setGeometry(850, 330, 150, 50)
        self.stopwatch_btn.clicked.connect(self.start_stopwatch)
        self.stopwatch_btn.setStyleSheet("""
            QPushButton {
                background-color: #222222;
                color: #F0F0F0;
                font: 17px;
                border: none;
            }
            QPushButton:hover {
                background-color: #242424;
            }
        """)

        self.pomodoro_btn = QPushButton(self, text="Pomodoro")
        self.pomodoro_btn.setGeometry(1010, 330, 150, 50)
        self.pomodoro_btn.clicked.connect(self.pomodoro)
        self.pomodoro_btn.setStyleSheet("""
            QPushButton {
                background-color: #222222;
                color: #F0F0F0;
                font: 17px;
                border: none;
            }
            QPushButton:hover {
                background-color: #242424;
            }
        """)

        close_button = QPushButton("X", self)
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #FF6347; 
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #D32F2F; 
            }
        """)
        close_button.clicked.connect(self.close)

        minimize_button = QPushButton("-", self)
        minimize_button.setStyleSheet("""
            QPushButton {
                background-color: #1E90FF; 
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #1565C0; 
            }
        """)
        minimize_button.clicked.connect(self.showMinimized)

        title_bar = QHBoxLayout()
        title_bar.addWidget(minimize_button)
        title_bar.addStretch(1)
        title_bar.addWidget(close_button)

        self.layout.addLayout(title_bar)

        self.label = QLabel(self)
        self.label.setGeometry(870, 385, 300, 200)
        self.label.setText("0")
        self.label.setStyleSheet("background-color: #222222; color: white; font-size: 150px;")
        
        self.stop_btn = QPushButton(self, text="Dur")
        self.stop_btn.clicked.connect(self.stop)
        self.stop_btn.setGeometry(750, 640, 100, 50)
        self.stop_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; 
                border: 1px solid #4CAF50; 
                border-radius: 7px;
                color: white; 
                font-size: 16px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #45a049; 
                border-color: #45a049; 
            }
        """)
        self.stop_btn.hide()

        self.go_btn = QPushButton(self, text="Devam")
        self.go_btn.clicked.connect(self.go)
        self.go_btn.setGeometry(750, 640, 100, 50)
        self.go_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; 
                border: 1px solid #4CAF50; 
                border-radius: 7px;
                color: white; 
                font-size: 14px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #45a049; 
                border-color: #45a049; 
            }
        """)
        self.go_btn.hide()


        self.pomodoro_go_btn = QPushButton(self, text="Devam")
        self.pomodoro_go_btn.clicked.connect(self.go)
        self.pomodoro_go_btn.setGeometry(750, 640, 100, 50)
        self.pomodoro_go_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; 
                border: 1px solid #4CAF50; 
                border-radius: 7px;
                color: white; 
                font-size: 16px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #45a049; 
                border-color: #45a049; 
            }
        """)
        self.pomodoro_go_btn.hide()

        self.finish_btn = QPushButton(self, text="Bitir")
        self.finish_btn.clicked.connect(self.finish)
        self.finish_btn.setGeometry(890, 640, 100, 50)
        self.finish_btn.setStyleSheet("""
            QPushButton {
                background-color: #8B0000; 
                border: 1px solid #8B0000; 
                border-radius: 7px;
                color: white; 
                font-size: 16px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #800000; 
                border-color: #800000; 
            }
        """)
        self.finish_btn.hide()

        self.format_btn = QPushButton(self, text="Sıfırla")
        self.format_btn.clicked.connect(self.format_)
        self.format_btn.setGeometry(1030, 640, 100, 50)
        self.format_btn.setStyleSheet("""
            QPushButton {
                background-color: #1565C0;
                border: 1px solid #1565C0; 
                border-radius: 7px;
                color: white;
                font-size: 16px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #0D47A1;
                border-color: #0D47A1; 
            }
        """)
        self.format_btn.hide()

        self.pomodoro = QComboBox(self)
        self.pomodoro.setGeometry(875, 640, 150, 50)
        self.pomodoro.addItems(["Pomodoro Süresi", "1 dk", "10 dk", "15 dk", "20 dk", "30 dk", "45 dk", "1 saat", "1 saat 30 dk", "1 saat 45 dk", "2 saat", "2 saat 30 dk", "3 saat", "5 saat"])
        self.pomodoro.setStyleSheet("background-color: purple; color: black; border: 20 px ")
        self.pomodoro.hide()

        self.pomodoro_go_btn = QPushButton(self, text="Başlat")
        self.pomodoro_go_btn.clicked.connect(self.pomodoro_go)
        self.pomodoro_go_btn.setGeometry(740, 640, 100, 50)
        self.pomodoro_go_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; 
                border: 1px solid #4CAF50; 
                border-radius: 7px;
                color: white; 
                font-size: 16px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #45a049; 
                border-color: #45a049; 
            }
        """)
        self.pomodoro_go_btn.hide()

        self.pomodoro_stop_btn = QPushButton(self, text="Dur")
        self.pomodoro_stop_btn.clicked.connect(self.pomodoro_stop)
        self.pomodoro_stop_btn.setGeometry(740, 640, 100, 50)
        self.pomodoro_stop_btn.setStyleSheet("""
            QPushButton {
                background-color: #1565C0;
                border: 1px solid #1565C0; 
                border-radius: 7px;
                color: white;
                font-size: 16px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #0D47A1;
                border-color: #0D47A1; 
            }
        """)
        self.pomodoro_stop_btn.hide()

        self.format_pomodoro_btn = QPushButton(self, text="Sıfırla")
        self.format_pomodoro_btn.clicked.connect(self.format_pomodoro)
        self.format_pomodoro_btn.setGeometry(1060, 640, 100, 50)
        self.format_pomodoro_btn.setStyleSheet("""
            QPushButton {
                background-color: #1565C0;
                border: 1px solid #1565C0; 
                border-radius: 7px;
                color: white;
                font-size: 16px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #0D47A1;
                border-color: #0D47A1; 
            }
        """)
        self.format_pomodoro_btn.hide()

        self.music_btn = QPushButton(self, text="Dinle")
        self.music_btn.clicked.connect(self.music)
        self.music_btn.setGeometry(1770, 1000, 100, 50)
        self.music_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; 
                color: white;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: purple; 
            }
        """)
        self.music_btn.hide()

        self.music_stop_btn = QPushButton(self, text="Dur")
        self.music_stop_btn.clicked.connect(self.music_stop)
        self.music_stop_btn.setGeometry(1770, 1000, 100, 50)
        self.music_stop_btn.setStyleSheet("""
            QPushButton {
                background-color: green; 
                color: white;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: red; 
            }
        """)
        self.music_stop_btn.hide()

    def settings(self):
        self.settings_btn.hide()
        self.light_btn.show()
        self.dark_btn.show()
        self.langue_e_btn.show()
        self.langue_a_btn.show()
        self.settings_hide_btn.show()

    def settings_hide(self):
        self.settings_btn.show()
        self.light_btn.hide()
        self.dark_btn.hide()
        self.langue_e_btn.hide()
        self.langue_a_btn.hide()
        self.settings_hide_btn.hide()

    
    def light(self):
        self.setStyleSheet("background-color: white;")
        self.main_btn.setStyleSheet("background-color:  #DCDCDC")
        self.timer_btn.setStyleSheet("background-color: #DCDCDC; color: black; border:none; font-size: 17px;")
        self.timer_btn.setStyleSheet("""
            .QPushButton {
                background-color: #DCDCDC;
                border: none;
            }                     
            .QPushButton:hover {
                background-color: #F0F0F0;
                border: none;
            }
         """)
        self.pomodoro_btn.setStyleSheet("background-color: #DCDCDC; color: black; border:none; font-size: 17px;")
        self.pomodoro_btn.setStyleSheet("""
            .QPushButton {
                background-color: #DCDCDC;
                border: none;
            }                     
            .QPushButton:hover {
                background-color: #F0F0F0;
                border: none;
            }
        """)
        self.stopwatch_btn.setStyleSheet("background-color: #DCDCDC; color: black; border:none; font-size: 17px;")
        self.stopwatch_btn.setStyleSheet("""
            .QPushButton {
                background-color: #DCDCDC;
                border: none;
            }                     
            .QPushButton:hover {
                background-color: #F0F0F0;
                border: none;
            }
        """)
        self.label.setStyleSheet("background-color: #DCDCDC; font-size: 150px; ")

    def dark(self):
        self.setStyleSheet("background-color: #1A1A1A;")
        self.main_btn.setStyleSheet("background-color:  #222222")
        self.timer_btn.setStyleSheet("background-color: #222222; color: white; border:none; font-size: 17px;")
        self.pomodoro_btn.setStyleSheet("background-color: #222222; color: white; border:none; font-size: 17px;")
        self.stopwatch_btn.setStyleSheet("background-color: #222222; color: white; border:none; font-size: 17px;")
        self.label.setStyleSheet("background-color: #222222; color: white; font-size: 150px;")

    def langue_e(self):
        self.timer_btn.setText("Time")
        self.pomodoro_btn.setText("Pomodoro")
        self.stopwatch_btn.setText("Stopwatch")
        self.stop_btn.setText("Start")
        self.stop_btn.setText("Stop")
        self.finish_btn.setText("End")
        self.music_btn.setText("Music")
        self.pomodoro_go_btn.setText("Start")
        self.format_pomodoro_btn.setText("Reset")
        self.format_btn.setText("Reset")
        self.go_btn.setText("Contınue")

    def langue_a(self):
        self.timer_btn.setText("وقت")
        self.pomodoro_btn.setText("بومودورو")
        self.stopwatch_btn.setText("ساعة التوقيف")
        self.stop_btn.setText("ابتداء")
        self.stop_btn.setText("قف")
        self.finish_btn.setText("انهها")
        self.music_btn.setText("موسيقى")
        self.pomodoro_go_btn.setText("ابتداء")
        self.format_pomodoro_btn.setText("إعادة ضبط")
        self.format_btn.setText("إعادة ضبط")
        self.go_btn.setText("أكمل")


    def timer(self):
        self.stop_btn.hide()
        self.format_pomodoro_btn.hide()
        self.music_btn.hide()
        self.music_stop_btn.hide()
        self.pomodoro.hide()
        self.pomodoro_go_btn.hide()
        self.format_btn.hide()
        self.finish_btn.hide()
        self.stop_btn.hide()
        self.go_btn.hide()

        simdi = datetime.now()
        saat = simdi.hour
        dakika = simdi.minute
        saniye = simdi.second
        
        self.label.setGeometry(650, 400, 600, 200)
        #self.label.setStyleSheet("font-size: 100px;")
        self.label.setText(f"{saat:02d}:{dakika:02d}:{saniye:02d}")
        

    def stop(self):
        self.timer.stop()
        self.go_btn.show()

    def go(self):
        self.label.setGeometry(875, 385, 300, 200)
        self.label.setText("")
        self.timer.start(1000)
        self.timer.start(1000)
        self.stop_btn.show()
        self.finish_btn.show()
        self.go_btn.hide()
        self.pomodoro_stop_btn.hide()
        self.pomodoro_go_btn.hide()

    def finish(self):
        self.timer.stop()
        self.counter = 0
        self.label.setText("0")
        self.go_btn.show()
        
    def format_(self):
        self.timer.stop()
        self.counter = -1
        self.counter += 1
        self.label.setText("0")

    def start_stopwatch(self):
        self.stop_btn.hide()
        self.go_btn.show()
        self.finish_btn.show()
        self.format_btn.show()
        self.pomodoro.hide()
        self.format_pomodoro_btn.hide()
        self.music_btn.hide()
        self.pomodoro_stop_btn.hide()
        self.pomodoro_go_btn.hide()
        self.pomodoro_go_btn.hide()
        
    def update_label(self):
        self.counter += 1
        self.label.setText(str(self.counter))

    def pomodoro(self):
        self.label.setGeometry(770, 385, 405, 200)
        self.label.setText("")
        
        self.pomodoro.show()
        self.pomodoro_go_btn.show()
        self.format_pomodoro_btn.show()
        self.stop_btn.hide()
        self.finish_btn.hide()
        self.format_btn.hide()
        self.music_btn.show()

    def update_label_pomodoro(self):
        self.counter_pomodoro -= 1
        self.label.setText(str(self.counter_pomodoro))
        if self.counter_pomodoro <= 0:
            self.timer_pomodoro.stop()
            self.message_signal.emit()

    def pomodoro_go(self):
        süre = self.pomodoro.currentText()
        try:
            if süre == "1 dk":
                self.counter_pomodoro = 60
            elif süre == "10 dk":
                self.counter_pomodoro = 6000
            elif süre == "15 dk":
                self.counter_pomodoro = 900
            elif süre == "20 dk":
                self.counter_pomodoro = 1200
            elif süre == "30 dk":
                self.counter_pomodoro = 1800
            elif süre == "45 dk":
                self.counter_pomodoro = 2700
            elif süre == "1 saat":
                self.counter_pomodoro = 3600
            elif süre == "1 saat 30 dk":
                self.counter_pomodoro = 5400
            elif süre == "1 saat 45 dk":
                self.counter_pomodoro = 6300
            elif süre == "2 saat":
                self.counter_pomodoro = 7200
            elif süre == "2 saat 30 dk":
                self.counter_pomodoro = 9000
            elif süre == "3 saat":
                self.counter_pomodoro = 10800
            elif süre == "5 saat":
                self.counter_pomodoro = 18000
            else:
                self.label.setText("error")
                return
            
            self.timer_pomodoro.start(1000)
            self.label.setText(str(self.counter_pomodoro))
            
        except Exception as e:
            print(f"Error: {e}")

        self.pomodoro_go_btn.hide()
        self.pomodoro_stop_btn.show()

    def show_message(self):
        self.music()
        QMessageBox.information(self, "Süre Doldu", "Tebrikler!\nPomodoro hedefinizi başarıyla gerçekleştirdiniz.")

    def pomodoro_stop(self):
        self.pomodoro_go_btn.show()
        self.pomodoro_stop_btn.hide()
        self.timer_pomodoro.stop()

    def format_pomodoro(self):
        self.timer_pomodoro.stop()
        self.counter_pomodoro = 0  
        self.label.setText("0")  
        self.format_pomodoro_btn.show()

    def music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play()
        self.music_btn.hide()
        self.music_stop_btn.show()

    def music_stop(self):
        pygame.mixer.music.stop()
        self.music_btn.show()
        self.music_stop_btn.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    timer = Timer()
    timer.showFullScreen()
    sys.exit(app.exec_())
