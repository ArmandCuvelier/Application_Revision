import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout,QPushButton, QLineEdit, QListWidget, QLabel,QMessageBox, QInputDialog, QTextEdit
from PyQt6.QtCore import Qt

"""
This views is the first interface of the application who allows the user to choose beetween : 
- Create a course
- Modify a course to add or remove questions
- Review the course in order to train
- Leave the application
"""
    
class ViewsBegin(QWidget):
    def __init__(self):
        super().__init__()
        
        # View settings
        self.setWindowTitle("Application de Révision - Home")
        self.resize(1000, 500)
        self.MainLayout = QVBoxLayout()
        
        # Separation of the MainLayout in layouts
        self.LTitle = QHBoxLayout()
        self.LActions = QHBoxLayout()
        self.LLeave = QHBoxLayout()
        
        # Layout of the Title
        self.Title = QLabel("Application de Révision")
        self.Title.setStyleSheet("font-size :50px;")
        self.LTitle.addWidget(self.Title,alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Layout of the actions
        self.LActions.setSpacing(0)
        self.create = QPushButton("Create a course")
        self.create.setStyleSheet(self.button_style_actions())
        self.modify = QPushButton("Modify a course")
        self.modify.setStyleSheet(self.button_style_actions())
        self.train = QPushButton("Train a course")
        self.train.setStyleSheet(self.button_style_actions())
        self.LActions.addWidget(self.create,alignment=Qt.AlignmentFlag.AlignCenter)
        self.LActions.addWidget(self.modify,alignment=Qt.AlignmentFlag.AlignCenter)
        self.LActions.addWidget(self.train,alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Layout for leavec the application
        self.leave = QPushButton("Leave")
        self.leave.setStyleSheet(self.button_style_leave())
        self.leave.clicked.connect(self.close)
        self.LLeave.addWidget(self.leave,alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Assembly in the Main layout
        self.MainLayout.addLayout(self.LTitle)
        self.MainLayout.addLayout(self.LActions)
        self.MainLayout.addLayout(self.LLeave)

        # Finalisation of the initialisation
        self.setLayout(self.MainLayout)
        self.setStyleSheet("font-family : Open Sans	;background-color : #dceefc;color : black;")
        
    # Style of the button of the layout of actions
    def button_style_actions(self):
        return """
            QPushButton {
                background-color: #2196F3;
                border-radius: 7px;
                font-size: 20px;
                width : 200px;
                height : 50px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """
    # Style of the button leave
    def button_style_leave(self):
        return """
            QPushButton {
                background-color: #000000;
                color : white;
                border-radius: 2px;
                font-size: 10px;
                width : 100px;
                height : 25px;
            }
            QPushButton:hover {
                background-color: #222222;
            }
        """   

# Tests
if __name__ == "__main__":
    app = QApplication(sys.argv)
    views = ViewsBegin()
    views.show()
    sys.exit(app.exec())