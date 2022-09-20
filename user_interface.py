# importing the required libraries

from tkinter import Button
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from dc_motors import forward, backward, turn_left, turn_right, stop
import calculate
import sys
import time

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

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

        # Buttons

        button_up = QPushButton(self)

        button_down = QPushButton(self)

        button_left = QPushButton(self)

        button_right = QPushButton(self)

        command_button = QPushButton(self)

        safe_keeping_button = QPushButton("Safe - Keeping", self)

        safe_guard_button = QPushButton("Safe - Guard", self)

        fall_detection_button = QPushButton("Fall - Detection", self)

        spy_mode_button = QPushButton("Spy Mode", self)

        # Geometry

        button_up.setGeometry(150, 150, 100, 100)

        button_down.setGeometry(150, 350, 100, 100)

        button_left.setGeometry(50, 250, 100, 100)

        button_right.setGeometry(250, 250, 100, 100)

        command_button.setGeometry(900,150,50,50)

        self.command_box.setGeometry(450,150,400,50)

        title.setGeometry(300,0,500,120)

        mode.setGeometry(615,200,100,100)

        safe_keeping_button.setGeometry(450,300,180,50)

        safe_guard_button.setGeometry(670,300,180,50)

        fall_detection_button.setGeometry(450,400,180,50)

        spy_mode_button.setGeometry(670,400,180,50)

        # Connect to function

        button_up.clicked.connect(self.robot_move_forward)

        button_down.clicked.connect(self.robot_move_backward)

        button_left.clicked.connect(self.robot_turn_left)

        button_right.clicked.connect(self.robot_turn_right)

        command_button.clicked.connect(self.retrieve_command)

        # Button image

        button_up.setStyleSheet("background-image : url(interface-images/up-arrow.png); border-image: url(interface-images/up-arrow.png)")

        button_down.setStyleSheet("background-image : url(interface-images/down-arrow.png); border-image: url(interface-images/down-arrow.png)")

        button_left.setStyleSheet("background-image : url(interface-images/left-arrow.png); border-image: url(interface-images/left-arrow.png)")

        button_right.setStyleSheet("background-image : url(interface-images/right-arrow.png); border-image: url(interface-images/right-arrow.png)")

        command_button.setStyleSheet("background-image : url(interface-images/upload.png); border-image: url(interface-images/upload.png)")


    def robot_move_forward(self):
    
        print("Moving forward")

        forward()

    def robot_move_backward(self):
    
        print("Moving backward")

        backward()

    def robot_turn_left(self):

        print("Turning left")

        turn_left()

    def robot_turn_right(self):
    
        print("Turning right")

        turn_right()

    def retrieve_command(self):

        command = self.command_box.text()

        self.command_box.setText("")

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
