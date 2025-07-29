import sys
import json
import os
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from Views.ViewsBegin import ViewsBegin
from Views.ViewsCreation import ViewsCreation
from Widgets.WidgetQuestions import WidgetQuestions

"""
This controller connect the Views and the course
"""

class Controller:
    def __init__(self):
        # Initialisation of the views
        self.Views_Begin = ViewsBegin()
        self.Views_Creation = ViewsCreation()
        self.Views_Modification = ViewsCreation()
        
        # Initialisation of a list who contains the question/answers
        self.questions = []
        
        # Signal of the views Begin
        self.Views_Begin.create.clicked.connect(lambda : self.navigate(self.Views_Creation))
        self.Views_Begin.modify.clicked.connect(lambda : self.ouverture())
        
        # Signal of the wiews Creation
        self.Views_Creation.back.clicked.connect(lambda: self.comeback(self.Views_Creation))
        self.Views_Creation.save.clicked.connect(lambda: self.save_json())
        
        # Signal of the views Modification
        
        
        # Execution
        self.Views_Begin.show()
        
    # Function who start the views of creation
    def navigate(self,views_direction : QWidget):
        self.Views_Begin.hide()
        views_direction.show()
        
    # Function who allows the user to come back at the first page    
    def comeback(self, from_view: QWidget):
        from_view.hide()
        self.questions.clear()
        self.Views_Begin.show()
    
    # Function who save the informations of the question into a list if the questions aren't empty
    def save_question(self):
        self.questions = []
        for i in range(self.Views_Creation.questions_layout.count()):
            widget = self.Views_Creation.questions_layout.itemAt(i).widget()
            if isinstance(widget, WidgetQuestions):
                prompt = widget.question.toPlainText().strip()
                answer = widget.answer.toPlainText().strip()
                if not prompt or not answer:
                    QMessageBox.warning(self.Views_Creation,"Error","Empty question(s)")
                    return False
                self.questions.append({"prompt": prompt, "answer": answer})
        return True
    
    # Function who save the course into a json. She verify if the form isn't empty
    def save_json(self):
        if not self.save_question():
            return
        name = self.Views_Creation.name_course.text().strip()
        if not name:
            QMessageBox.warning(self.Views_Creation, "Error", "The name of the course is empty")
            return
        data = {
            "name": name,
            "questions": self.questions
        }
        name = "Datas/"+data["name"] + ".json"
        try:
            with open(name, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            QMessageBox.information(self.Views_Creation, "Success", "The course is save")
        except Exception as e:
            QMessageBox.warning(self.Views_Creation, "Error", "Error in the save")
            
    # Function who open a course with a json file into a view
    def ouverture(self):
        self.questions.clear()
        try:
            filename, _ = QFileDialog.getOpenFileName(self.Views_Begin,"Open a json file","","File JSON (*.json)")
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            QMessageBox.warning(self.Views_Creation, "Error", "Error in the opening")
        self.navigate(self.Views_Modification)
        self.Views_Modification.name_course.setText(data["name"])
        self.questions = data["questions"]
        self.Views_Modification.nb_question.setText(str(len(self.questions))+" Question")
        for i in range(len(self.questions)):
            self.Views_Modification.addQuestions_completed(self.questions[i])
            
# Tests        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Controller = Controller()
    sys.exit(app.exec())