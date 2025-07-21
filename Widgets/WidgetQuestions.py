import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout,QPushButton, QLineEdit, QListWidget, QLabel,QMessageBox, QInputDialog, QTextEdit
from PyQt6.QtCore import Qt

"""
This widget allows to contain a question and an answer.
It can be add once or multiply in the ViewsCreation and ViewsModification
"""
class WidgetQuestions(QWidget):
    def __init__(self):
        super().__init__()
        
        # Widget settings
        self.resize(800,350)
        self.MainLayout = QVBoxLayout()
        
        # Widget of the question
        self.question = QTextEdit()
        self.question.setPlaceholderText("Question...")
        self.question.setStyleSheet("""
            background-color : #5b91cf;
            color : #FFFFFF;
            border : 1px solid #000000;
            border-radius : 8px;
        """)
        
        # Widget of the answer
        self.answer = QTextEdit()
        self.answer.setPlaceholderText("Answer...")
        self.answer.setStyleSheet("""
            background-color : #5b91cf;
            color : #FFFFFF;
            border : 1px solid #000000;
            border-radius : 8px;
        """)
        
        # Assembly in the Main layout
        self.MainLayout.addWidget(self.question)
        self.MainLayout.addWidget(self.answer)

        # Finalisation of the initialisation
        self.setLayout(self.MainLayout)
        self.setStyleSheet("""
            font-family : Open Sans	;
            background-color : #bdb7b7;
        """)
        
# Tests
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = WidgetQuestions()
    widget.show()
    sys.exit(app.exec())
        