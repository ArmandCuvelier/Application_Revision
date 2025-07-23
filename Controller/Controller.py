import sys
import json
import os
from PyQt6.QtWidgets import QApplication, QWidget
from Views.ViewsBegin import ViewsBegin
from Views.ViewsCreation import ViewsCreation

"""
This controller connect the Views and the course
"""

class Controller:
    def __init__(self):
        # Initialisation of the views
        self.Views_Begin = ViewsBegin()
        self.Views_Creation = ViewsCreation()
        
        # Signal of the views Begin
        self.Views_Begin.create.clicked.connect(lambda : self.navigate(self.Views_Creation))
        
        # Signal of the wiews Creation
        self.Views_Creation.back.clicked.connect(lambda: self.comeback(self.Views_Creation))
        
        # Execution
        self.Views_Begin.show()
        
    # Function who start the views of creation
    def navigate(self,views_direction : QWidget):
        self.Views_Begin.hide()
        views_direction.show()
        
    # Function who allows the user to come back at the first page    
    def comeback(self, from_view: QWidget):
        from_view.hide()
        self.Views_Begin.show()
        
        
# Tests        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Controller = Controller()
    sys.exit(app.exec())