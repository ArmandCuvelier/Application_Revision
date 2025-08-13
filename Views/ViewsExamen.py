import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget, QLabel, QMessageBox, QInputDialog, QTextEdit, QScrollArea, QSizePolicy
from PyQt6.QtCore import Qt

"""
This views is the interface who allows the user to test out his learnings with questions
"""
class ViewsExamen(QWidget):
    def __init__(self):
        super().__init__()
        
        # View settings
        self.resize(1000, 500)
        self.MainLayout = QVBoxLayout()
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout.setSpacing(0)
        
        # Separation of the MainLayout in layouts and Widgets
        self.WHeader = QWidget()
        self.WResults = QWidget()
        self.WTraining = QWidget()
        
        # Widget of the header
        self.LHeader = QHBoxLayout()
        self.LHeader.setContentsMargins(20, 0, 20, 10)
        self.title = QLabel("Course Review Application")
        self.LHeader.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.WHeader.setLayout(self.LHeader)
        self.WHeader.setStyleSheet(self.style_widget_title())
        
        # Widget of the Trainings
        self.WTraining.setStyleSheet(self.style_widget_test())
        self.LTraining = QVBoxLayout()
        self.prompt = QLabel()
        self.prompt.setStyleSheet(self.style_prompt())
        self.answer = QLineEdit()
        self.answer.setStyleSheet(self.style_answer())
        self.next = QPushButton("Next Question")
        self.next.setStyleSheet(self.button_style())
        self.LTraining.addWidget(self.prompt,5)
        self.LTraining.addStretch(1)
        self.LTraining.addWidget(self.answer,7)
        self.LTraining.addStretch(1)
        self.LTraining.addWidget(self.next,5)
        self.LTraining.addStretch(1)
        self.WTraining.setLayout(self.LTraining)
        self.LTraining.addStretch(1)
        
        # Widget of the results
        self.WResults.setStyleSheet(self.style_widget_test())
        self.LResults = QVBoxLayout()
        self.title_course = QLabel()
        self.title_course.setStyleSheet(self.style_title())
        self.title_course.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.score = QLabel()
        self.score.setStyleSheet(self.style_results())
        self.score.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.finish = QPushButton("Finish the course")
        self.finish.setStyleSheet(self.button_style())
        self.LResults.addStretch(1)
        self.LResults.addWidget(self.title_course,2)
        self.LResults.addWidget(self.score,8)
        self.LResults.addStretch(1)
        self.LResults.addWidget(self.finish,4)
        self.LResults.addStretch(1)
        self.WResults.setLayout(self.LResults)
        self.LResults.addStretch(1)

        
        # Assembly in the Main layout
        self.MainLayout.addWidget(self.WHeader,1)
        self.MainLayout.addWidget(self.WResults,4)
        self.MainLayout.addWidget(self.WTraining,4)
        
        # Finalisation of the initialisation
        self.setLayout(self.MainLayout)
        self.setStyleSheet("""
            font-family: Open Sans;
            background-color: #5f90b9;
            color: black;
            margin: 0;
            padding: 0;
        """)
    
    # Style of the Test
    def style_widget_test(self):
        return """
        QWidget {
            background-color: #e5f3ff;
            color : #000000;
            margin : 30%;
            border-radius : 10px;
        }
    """
    
    # Style of the rest of the button
    def style_widget_title(self):
        return """
        QWidget {
            color : #000000;
            font-size : 30px;
        }
    """
    def style_prompt(self):
        return """
        QLabel{
            background-color : #e5f3ff;
            color : #000000;
            font-size : 30px;
            font-weight : bold;
            margin : 30px 100px 0 100px;
        }
    """
    
    def style_answer(self):
        return """
        QLineEdit{
            background-color : #e5f3ff;
            border : 1px solid black;
            border-radius : 10px;
            color : #000000;
            font-size : 40px;
            height : 50px;
            margin : 0 100px 0 100px;
        }
    """
    
    def style_title(self):
        return """
        QLabel{
            background-color : #e5f3ff;
            color : #000000;
            font-size : 30px;
            font-weight : bold;
            margin : 30px 100px 0 100px;
        }
    """
    
    def style_results(self):
        return """
        QLabel{
            background-color : #e5f3ff;
            color : #000000;
            font-size : 20px;
            margin : 30px 100px 0 100px;
        }
    """
    
    def button_style(self):
        return """
            QPushButton {
                background-color: #5f90b9;
                color : #000000;
                border-radius: 7px;
                font-size: 20px;
                height : 50px;
                margin : 10px 270px 10px 270px;

            }
            QPushButton:hover {
                background-color: #4f8bbc;
            }
        """
        
# Tests
if __name__ == "__main__":
    app = QApplication(sys.argv)
    views = ViewsExamen()
    views.show()
    sys.exit(app.exec())