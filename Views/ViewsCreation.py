import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget, QLabel, QMessageBox, QInputDialog, QTextEdit, QScrollArea, QSizePolicy
from PyQt6.QtCore import Qt
from Widgets.WidgetQuestions import WidgetQuestions

"""
This views is the interface who allows the user to create a course and his questions in order to save it.
"""
class ViewsCreation(QWidget):
    def __init__(self):
        super().__init__()
        
        # Variable who contains the number of question of the course
        self.nb_questions = 0
        
        # View settings
        self.setWindowTitle("Application de Révision - Creation of a course")
        self.resize(1000, 500)
        self.MainLayout = QVBoxLayout()
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout.setSpacing(0)
                
        # Separation of the MainLayout in layouts and Widgets
        self.WHeader = QWidget()
        self.LCourse = QVBoxLayout()
        
        # layout of the header
        self.LHeader = QHBoxLayout()
        self.LHeader.setContentsMargins(20, 0, 20, 10)
        self.back = QPushButton("Back to the menu")
        self.back.setStyleSheet(self.button_style_header())
        self.title = QLabel("Course Review Application")
        self.title.setStyleSheet("font-size: 30px; margin: 0; padding: 0;")
        self.save = QPushButton("Save the course")
        self.save.setStyleSheet(self.button_style_header())
        self.LHeader.addWidget(self.back, alignment=Qt.AlignmentFlag.AlignLeft)
        self.LHeader.addStretch(1)
        self.LHeader.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.LHeader.addStretch(1)
        self.LHeader.addWidget(self.save, alignment=Qt.AlignmentFlag.AlignRight)
        self.WHeader.setLayout(self.LHeader)
        self.WHeader.setStyleSheet("border-bottom: 2px #FFFFFF solid; margin: 0; padding: 0;")
        
        # Header of the layout of the informations about the course
        self.Wheader_course = QWidget()
        self.Wheader_course.setStyleSheet("""
            margin-left: 30px;
            margin-right: 30px;
            margin-top: 0px;
            padding: 15px;
        """)
        self.Lheader_course = QHBoxLayout(self.Wheader_course)
        self.name_course = QLineEdit()
        self.name_course.setPlaceholderText("Name of the course")
        self.name_course.setFixedSize(400, 50)
        self.name_course.setStyleSheet("""
            QLineEdit {
                background-color: #170101;
                color: white;
                border: 1px solid #A3BFD9;
                border-radius: 8px;
                padding-left: 10px;
                font-size: 16px;
            }
            QLineEdit::placeholder {
                color: #CCCCCC;
            }
        """)
        self.nb_question = QLabel(str(self.nb_questions)+" Question")
        self.nb_question.setMinimumSize(150, 50)
        self.nb_question.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nb_question.setStyleSheet("""
            QLabel {
                background-color: #B8CCE2;
                color: #1A1A1A;
                font-size: 16px;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px 15px;
            }
        """)
        self.Lheader_course.addWidget(self.name_course)
        self.Lheader_course.addStretch(0)
        self.Lheader_course.addWidget(self.nb_question)
        
        # Information of the questions (questions_scroll is a scroll area for the WidgetQuestions)
        self.Lmain_course = QVBoxLayout()
        self.questions_scroll = QScrollArea()
        self.questions_scroll.setWidgetResizable(True)
        self.questions_scroll.setFixedHeight(250)
        self.questions_scroll.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.questions_container = QWidget()
        self.questions_layout = QVBoxLayout(self.questions_container)
        self.questions_scroll.setWidget(self.questions_container)
        self.add = QPushButton("Add a question")
        self.add.setStyleSheet(self.button_style_actions())
        self.add.clicked.connect(lambda : self.addQuestions())
        self.Lmain_course.addWidget(self.questions_scroll)
        self.Lmain_course.addWidget(self.add, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Assembly of the layout about the course
        self.LCourse.setSpacing(0)
        self.LCourse.setContentsMargins(0, 0, 0, 0)
        self.LCourse.addWidget(self.Wheader_course)
        self.LCourse.addLayout(self.Lmain_course)
        
        # Assembly in the Main layout
        self.MainLayout.addWidget(self.WHeader)
        self.MainLayout.addLayout(self.LCourse)

        # Finalisation of the initialisation
        self.setLayout(self.MainLayout)
        self.setStyleSheet("""
            font-family: Open Sans;
            background-color: #5f90b9;
            color: black;
            margin: 0;
            padding: 0;
        """)
        
    # Style of the button in the header
    def button_style_header(self):
        return """
            QPushButton {
                background-color: #e5f3ff;
                border-radius: 7px;
                font-size: 20px;
                width: 175px;
                height: 50px;
                margin: 0;
            }
            QPushButton:hover {
                background-color: #b0b8bf;
            }
        """
    
    # Style of the rest of the button
    def button_style_actions(self):
        return """
            QPushButton {
                background-color: #e5f3ff;
                border-radius: 7px;
                margin-left: 30px;
                margin-right: 30px;
                margin-bottom : 30px;
                font-size: 20px;
                min-width: 200px;
                height: 40px;
            }
            QPushButton:hover {
                background-color: #b0b8bf;
            }
        """
    
    # Add a question with the prompt and the answer if the precedent question isn't empty
    def addQuestions(self):
        for i in range(self.questions_layout.count()):
            widget = self.questions_layout.itemAt(i).widget()
            if isinstance(widget, WidgetQuestions):
                prompt = widget.question.toPlainText().strip()
                answer = widget.answer.toPlainText().strip()
                if not prompt or not answer:
                    QMessageBox.warning(self,"Error","There are one or multiply empty question")
                    return
        question_widget = WidgetQuestions()
        self.questions_layout.addWidget(question_widget)
        self.nb_questions+=1
        self.nb_question.setText(str(self.nb_questions)+" Question")
        
    # Add a question with the prompt and the answer (completed with the texts in parameters) if the precedent questions isn't empty
    def addQuestions_completed(self,dico : dict):
        for i in range(self.questions_layout.count()):
            widget = self.questions_layout.itemAt(i).widget()
            if isinstance(widget, WidgetQuestions):
                prompt = widget.question.toPlainText().strip()
                answer = widget.answer.toPlainText().strip()
                if not prompt or not answer:
                    QMessageBox.warning(self,"Error","There are one or multiply empty question")
                    return
        question_widget = WidgetQuestions()
        question_widget.question.setText(dico["prompt"])
        question_widget.answer.setText(dico["answer"])
        self.questions_layout.addWidget(question_widget)
        self.nb_questions+=1
        self.nb_question.setText(str(self.nb_questions)+" Question")


# Tests
if __name__ == "__main__":
    app = QApplication(sys.argv)
    views = ViewsCreation()
    views.show()
    sys.exit(app.exec())
