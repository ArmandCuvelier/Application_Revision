import sys
import json
import os
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from Views.ViewsBegin import ViewsBegin
from Views.ViewsCreation import ViewsCreation
from Views.ViewsExamen import ViewsExamen
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
        self.Views_Examen = ViewsExamen()
        
        # Initialisation of a list who contains the question/answers
        self.questions = []
        
        # Variable for the current index of questions
        self.question_index : int
        
        # List for the answers
        self.answers_questions = []
        
        # Signal of the views Begin
        self.Views_Begin.create.clicked.connect(lambda : self.navigate(self.Views_Creation))
        self.Views_Begin.modify.clicked.connect(lambda : self.ouverture())
        self.Views_Begin.train.clicked.connect(lambda: self.train())
        
        # Signal of the wiews Creation
        self.Views_Creation.back.clicked.connect(lambda: self.comeback(self.Views_Creation))
        self.Views_Creation.save.clicked.connect(lambda: self.save_json(self.Views_Creation))
        
        # Signal of the views Modification
        self.Views_Modification.back.clicked.connect(lambda: self.comeback(self.Views_Modification))
        self.Views_Modification.save.clicked.connect(lambda: self.save_json(self.Views_Modification))
        
        # Signal of the views Examen
        self.Views_Examen.next.clicked.connect(lambda: self.next_questions())
        self.Views_Examen.finish.clicked.connect(lambda: self.comeback(self.Views_Examen))
        
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
    def save_question(self,Views : ViewsCreation):
        self.questions = []
        for i in range(Views.questions_layout.count()):
            widget = Views.questions_layout.itemAt(i).widget()
            if isinstance(widget, WidgetQuestions):
                prompt = widget.question.toPlainText().strip()
                answer = widget.answer.toPlainText().strip()
                if not prompt or not answer:
                    QMessageBox.warning(Views,"Error","Empty question(s)")
                    return False
                self.questions.append({"prompt": prompt, "answer": answer})
        return True
    
    # Function who save the course into a json. She verify if the form isn't empty
    def save_json(self,Views : ViewsCreation):
        if not self.save_question(Views):
            return
        name = Views.name_course.text().strip()
        if not name:
            QMessageBox.warning(Views, "Error", "The name of the course is empty")
            return
        data = {
            "name": name,
            "questions": self.questions
        }
        name = "Datas/"+data["name"] + ".json"
        try:
            with open(name, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            QMessageBox.information(Views, "Success", "The course is save")
        except Exception as e:
            QMessageBox.warning(Views, "Error", "Error in the save")
            
    # Function who open a course with a json file into a view
    def ouverture(self):
        self.questions.clear()
        try:
            filename, _ = QFileDialog.getOpenFileName(self.Views_Begin,"Open a json file","","File JSON (*.json)")
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            QMessageBox.warning(self.Views_Creation, "Error", "Error in the opening")
            self.comeback(self.Views_Modification)
        self.navigate(self.Views_Modification)
        self.Views_Modification.name_course.setText(data["name"])
        self.questions = data["questions"]
        if len(self.questions)>=2:
            self.Views_Modification.nb_question.setText(str(len(self.questions))+" Questions")
        else :
            self.Views_Modification.nb_question.setText(str(len(self.questions))+" Questions")
        for i in range(len(self.questions)):
            self.Views_Modification.addQuestions_completed(self.questions[i])
        
    # Function who create the exam
    def train(self):
        self.questions.clear()
        try:
            filename, _ = QFileDialog.getOpenFileName(self.Views_Begin,"Open a json file","","File JSON (*.json)")
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            QMessageBox.warning(self.Views_Creation, "Error", "Error in the opening")
            self.comeback(self.Views_Examen)
        self.navigate(self.Views_Examen)
        self.Views_Examen.WResults.hide()
        self.Views_Examen.title_course.setText(data["name"])
        self.questions = data["questions"]
        self.answers_questions.clear()
        self.question_index = 0
        self.show_questions()
        
    def show_questions(self):
        self.Views_Examen.prompt.setText(self.questions[self.question_index]["prompt"])
        self.Views_Examen.answer.setText("")
        
    def next_questions(self):
        self.answers_questions.append(self.Views_Examen.answer.text().strip())
        if self.question_index >= len(self.questions) - 1:
            self.results()
            return
        self.question_index += 1
        self.show_questions()
    
    def results(self):
        self.Views_Examen.WTraining.hide()
        self.Views_Examen.WResults.show()
        results = 0
        for i in range(len(self.questions)):
            if self.questions[i]["answer"]==self.answers_questions[i] :
                results +=1
        self.Views_Examen.score.setText("Your score is " + str(results)+"/"+str(len(self.questions)))

# Tests        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Controller = Controller()
    sys.exit(app.exec())