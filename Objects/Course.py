class Course():
    
    """
    This class contains a course with questions and answers who are in a list
    Every course have a name
    """
    
    def __init__(self,name : str,listQuestions : list):
        self.name = name
        self.listQuestions = listQuestions
    
    # Return the name of the course
    def getNom(self):
        return self.name
    
    # Return the question
    def getQuestions(self,num : int):
        return self.listQuestions[num][0]
    
    # Return the answers
    def getAnswers(self,num : int):
        return self.listQuestions[num][1]
    
    # Add a question to the course
    def addQuestion(self, questions: str, answers: str):
        self.listQuestions.append((questions, answers))
        
    # Remove a question of a course
    def RemoveQuestion(self, questions : str, answers : str):
        self.listQuestions.remove((questions,answers))

# Tests
if __name__=="__main__":
    pass