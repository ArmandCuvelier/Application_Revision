import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout,QPushButton, QLineEdit, QListWidget, QLabel,QMessageBox, QInputDialog, QTextEdit
from PyQt6.QtCore import Qt

"""
This widget allows to contain a question and an answer.
It can be add once or multiply in the ViewsCreation and ViewsModification
"""
class WidgetQuestions(QWidget):
    def __init__(self,remove_fonction):
        super().__init__()
        
        # Widget settings
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
        
        # Widget of the remove button
        self.remove = QPushButton("Remove")
        self.remove.setStyleSheet(self.button_style_actions())
        self.remove.clicked.connect(lambda: remove_fonction(self))
        
        # Assembly in the Main layout
        self.MainLayout.addWidget(self.question)
        self.MainLayout.addWidget(self.answer)
        self.MainLayout.addWidget(self.remove)

        # Finalisation of the initialisation
        self.setLayout(self.MainLayout)
        self.setStyleSheet("""
            font-family : Open Sans	;
            background-color : #bdb7b7;
        """)
        
    # Style of the button of the layout of actions
    def button_style_actions(self):
        return """
            QPushButton {
                background-color: #e5f3ff;
                border-radius: 5px;
                font-size: 20px;
                width : 20px;
                height : 50px;
            }
            QPushButton:hover {
                background-color: #b0b8bf;
            }
        """
        
# Tests
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = WidgetQuestions()
    widget.show()
    sys.exit(app.exec())
        