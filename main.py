import sys
from PyQt6.QtWidgets import QApplication
from Controller.Controller import Controller

version = 1.0
logo = "images/logo.png"

if __name__ == "__main__":
    application_révision = QApplication(sys.argv)
    Controller = Controller(version, logo)
    sys.exit(application_révision.exec())