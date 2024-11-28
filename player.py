from questions import questions
from multi_answer_questions import multi_answer_questions
from fill_in_the_blank_questions import fill_in_the_blank_questions

class Player:
    
    def __init__(self, name = ""):
        self.name = name
        self.score = 0
        self.total_score = 0


    def __repr__(self):
        rounded_score = round(self.total_score)
        if self.total_score < 60:
            return f"Hey, {self.name}! You have a total score of {rounded_score}% and received an F on this exam. Unfortunately, you did not pass. Study the subject material and better luck next time!"
        elif self.total_score >= 60 and self.total_score<70:
            return f"Hey, {self.name}! You have a total score of {rounded_score}% and received a D on this exam. Contratulations, you passed!"
        elif self.total_score >= 70 and self.total_score < 80:
            return f"Hey, {self.name}! You have a total score of {rounded_score}% and received a C on this exam. Contratulations, you passed!"
        elif self.total_score >= 80 and self.total_score < 90:
            return f"Hey, {self.name}! You have a total score of {rounded_score}% and received a B on this exam. Contratulations, you passed!"
        else:
            return f"Hey, {self.name}! You have a total score of {rounded_score}% and received an A on this exam. Contratulations, you passed!"
        
    def update_total_score(self):
        self.total_score = (self.score / (len(questions) + len(multi_answer_questions) + len(fill_in_the_blank_questions))) * 100
