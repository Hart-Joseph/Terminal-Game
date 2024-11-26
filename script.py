from questions import questions
from multi_answer_questions import multi_answer_questions

class Player:
    
    def __init__(self, name = ""):
        self.name = name
        self.score = 0
        self.total_score = 0


    def __repr__(self):
        if self.total_score < 60:
            return f"Hey, {self.name}! You have a total score of {self.total_score}% and received an F on this exam. Unfortunately, you did not pass. Study the subject material and better luck next time!"
        elif self.total_score >= 60 and self.total_score<70:
            return f"Hey, {self.name}! You have a total score of {self.total_score}% and received a D on this exam. Contratulations, you passed!"
        elif self.total_score >= 70 and self.total_score < 80:
            return f"Hey, {self.name}! You have a total score of {self.total_score}% and received a C on this exam. Contratulations, you passed!"
        elif self.total_score >= 80 and self.total_score < 90:
            return f"Hey, {self.name}! You have a total score of {self.total_score}% and received a B on this exam. Contratulations, you passed!"
        else:
            return f"Hey, {self.name}! You have a total score of {self.total_score}% and received an A on this exam. Contratulations, you passed!"
        
    def update_total_score(self):
        self.total_score = (self.score / (len(questions) + len(multi_answer_questions))) * 100


# player1 = Player()
# player1.name = input("Hey, there! Thank you for taking the time to sit down and take a nursing proficiency exam. May I ask you to please enter your name?\nName: ")
# print(f"It's a pleasure to meet you, {player1.name}. I hope that you will enjoy this test that is comprised of {len(questions)} questions.")

# for i in range(len(questions)):
#     print(questions[i].get("Question"))
#     print("A: " + questions[i].get("A"))
#     print("B: " + questions[i].get("B"))
#     print("C: " + questions[i].get("C"))
#     print("D: " + questions[i].get("D"))
#     player_answer = input("Enter your answer: ")
#     while player_answer.upper() not in questions[i]:
#         player_answer = input("That is not a valid entry. Please enter an answer from A to D: ")
#     if questions[i].get("Answer") == player_answer.upper():
#         player1.score += 1
#         player1.update_total_score()
#         print("Correct!\n")
#     else:
#         print(f"The correct answer is {questions[i].get("Answer")}\n")

# print(player1)

for i in range(len(multi_answer_questions)):
    print(f"Question #{i + 1}:")
    print(f"{multi_answer_questions[i].get("Question")}\n")
    for option, answer in multi_answer_questions[i]["Options"].items():
        print(f"{option}: {answer}\n")
    print("Please enter your answers seperated by a space (e.g. 'A B C')")
    player_answer = input("Your answer: ")
    answer_list = player_answer.upper().split()
    while not all(multi_answer_questions[i]["Options"] for answer in answer_list):
        player_answer = input("Please enter a valid response:")
        player_answer = input("Your answer: ")
        answer_list = player_answer.upper().split()
    correct_answers_list = multi_answer_questions[i]["CorrectAnswers"]
    correct_answers = " ".join(correct_answers_list)
    if sorted(answer_list) == sorted(correct_answers_list):
        print("Correct!\n")
    else:
        print(f"The correct answers were {correct_answers}\n")
    
    