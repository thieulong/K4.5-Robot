# importing the required libraries

from tkinter import Button
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from dc_motors import forward, backward, turn_left, turn_right, stop
import calculate
import play_sound
import time
import os
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.engine_flag = 0

        self.setStyleSheet("background-color: white;")

        self.setWindowTitle("K4.5")

        self.setGeometry(100, 100, 1000, 550)

        self.UiComponents()

        self.update()

        self.show()


    def UiComponents(self):

        # Title

        title = QLabel("K4.5 - The Rover Pet", self)

        title.setFont(QFont('Arial', 30))

        # Mode

        mode = QLabel("Mode", self)

        mode.setFont(QFont('Arial', 20))

        # Command box

        self.command_box = QLineEdit(self)
        
        self.command_box.setPlaceholderText("Enter command")

        # Label

        self.label = QLabel(self)

        status = QPixmap("interface-images/engine_stop.jpg")

        self.label.setPixmap(status)

        self.label.setGeometry(300,150,50,50)

        # Buttons

        button_start_stop = QPushButton(self)

        button_up = QPushButton(self)

        button_down = QPushButton(self)

        button_left = QPushButton(self)

        button_right = QPushButton(self)

        button_stop = QPushButton(self)

        command_button = QPushButton(self)

        safe_keeping_button = QPushButton("Safe - Keeping", self)

        safe_guard_button = QPushButton("Safe - Guard", self)

        fall_detection_button = QPushButton("Fall - Detection", self)

        spy_mode_button = QPushButton("Spy Mode", self)

        # Geometry

        button_start_stop.setGeometry(50,150,100,100)

        button_up.setGeometry(150, 150, 100, 100)

        button_down.setGeometry(150, 350, 100, 100)

        button_left.setGeometry(50, 250, 100, 100)

        button_right.setGeometry(250, 250, 100, 100)

        button_stop.setGeometry(150,250,100,100)

        command_button.setGeometry(900,150,50,50)

        self.command_box.setGeometry(450,150,400,50)

        title.setGeometry(300,0,500,120)

        mode.setGeometry(615,200,100,100)

        safe_keeping_button.setGeometry(450,300,180,50)

        safe_guard_button.setGeometry(670,300,180,50)

        fall_detection_button.setGeometry(450,400,180,50)

        spy_mode_button.setGeometry(670,400,180,50)

        # Connect to function

        button_start_stop.clicked.connect(self.start_stop_engine)

        button_up.clicked.connect(self.robot_move_forward)

        button_down.clicked.connect(self.robot_move_backward)

        button_left.clicked.connect(self.robot_turn_left)

        button_right.clicked.connect(self.robot_turn_right)

        button_stop.clicked.connect(self.robot_stop)

        command_button.clicked.connect(self.retrieve_command)

        safe_keeping_button.clicked.connect(self.robot_safe_keeping)

        safe_guard_button.clicked.connect(self.robot_safe_guard)

        fall_detection_button.clicked.connect(self.robot_fall_detect)

        spy_mode_button.clicked.connect(self.robot_spy_mode)

        # Button image

        button_start_stop.setStyleSheet("background-image : url(interface-images/start_stop_button.jpg); border-image: url(interface-images/start_stop_button.jpg)")

        button_up.setStyleSheet("background-image : url(interface-images/up-arrow.png); border-image: url(interface-images/up-arrow.png)")

        button_down.setStyleSheet("background-image : url(interface-images/down-arrow.png); border-image: url(interface-images/down-arrow.png)")

        button_left.setStyleSheet("background-image : url(interface-images/left-arrow.png); border-image: url(interface-images/left-arrow.png)")

        button_right.setStyleSheet("background-image : url(interface-images/right-arrow.png); border-image: url(interface-images/right-arrow.png)")

        button_stop.setStyleSheet("background-image : url(interface-images/stop_button.jpg); border-image: url(interface-images/stop_button.jpg)")

        command_button.setStyleSheet("background-image : url(interface-images/upload.png); border-image: url(interface-images/upload.png)")

    
    def start_stop_engine(self):
        
        if self.engine_flag == 0:

            status = QPixmap("interface-images/engine_start.png")

            self.engine_flag += 1

            self.label.setPixmap(status)

            play_sound.play_sound_effect(sound=play_sound.start_engine)

        elif self.engine_flag == 1:

            self.engine_flag -= 1

            status = QPixmap("interface-images/engine_stop.jpg")

            self.label.setPixmap(status)

    def robot_stop(self):

        if self.engine_flag == 1:

            print("Stopped moving")

            stop()

    def robot_move_forward(self):

        if self.engine_flag == 1:
    
            print("Moving forward")

            forward()

    def robot_move_backward(self):

        if self.engine_flag == 1:
    
            print("Moving backward")

            backward()

    def robot_turn_left(self):

        if self.engine_flag == 1:

            print("Turning left")

            turn_left()

    def robot_turn_right(self):

        if self.engine_flag == 1:
    
            print("Turning right")

            turn_right()

    def robot_safe_keeping(self):

        os.system('python3 ~/RPI-Project-Rover/safe_keeping.py')

    def robot_safe_guard(self):

        os.system('python3 ~/RPI-Project-Rover/safe_guard.py')

    def robot_fall_detect(self):

        os.system('python3 ~/RPI-Project-Rover/fall_detection.py')

    def robot_spy_mode(self):

        os.system('python3 ~/RPI-Project-Rover/spy_mode.py')

    def retrieve_command(self):

        command = self.command_box.text()

        self.command_box.setText("")

        if self.engine_flag == 1:

            if any(word in command.lower() for word in ["+"]): calculate.addition(command)
                
            if any(word in command.lower() for word in ["-"]): calculate.subtraction(command)
                
            if any(word in command.lower() for word in ["*", "x"]): calculate.multiplication(command)
                
            if any(word in command.lower() for word in [":", "/"]): calculate.division(command)  
                                
            if any(word in command.lower() for word in ["forward"]):

                duration = [int(s) for s in command.split() if s.isdigit()][-1]

                forward()

                time.sleep(duration)

                stop()

            if any(word in command.lower() for word in ["backward"]):
        
                duration = [int(s) for s in command.split() if s.isdigit()][-1]

                backward()

                time.sleep(duration)

                stop()

            if any(word in command.lower() for word in ["left"]):
        
                duration = [int(s) for s in command.split() if s.isdigit()][-1]

                turn_left()

                time.sleep(duration)

                stop()

            if any(word in command.lower() for word in ["right"]):
        
                duration = [int(s) for s in command.split() if s.isdigit()][-1]

                turn_right()

                time.sleep(duration)

                stop()

App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())
