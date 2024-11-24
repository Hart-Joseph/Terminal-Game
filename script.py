class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0

    def __repr__(self):
        if self.score < 60:
            print(f"{self.name} has a total score of {self.score} and received an F on this exam. Unfortunately, you did not pass. Study the subject material and better luck next time!")
        elif self.score >= 60 and self.score<70:
            print(f"{self.name} has a total score of {self.score} and received a D on this exam. Contratulations, you passed!")
        elif self.score >= 70 and self.score < 80:
            print(f"{self.name} has a total score of {self.score} and received a C on this exam. Contratulations, you passed!")
        elif self.score >= 80 and self.score < 90:
            print(f"{self.name} has a total score of {self.score} and received a B on this exam. Contratulations, you passed!")
        else:
            print(f"{self.name} has a total score of {self.score} and received an A on this exam. Contratulations, you passed!")