class Question():
    
    """
    This class contains a question and an answer
    """
    
    def __init__(self,promt : str,answer : str):
        self.promt = promt
        self.answer = answer

    # Return the promt
    def getPromt(self):
        return self.promt
    
    # Return the answers
    def getAnswers(self):
        return self.answer