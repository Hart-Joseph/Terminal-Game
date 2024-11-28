from questions import questions
from multi_answer_questions import multi_answer_questions
from fill_in_the_blank_questions import fill_in_the_blank_questions
from player import Player


player1 = Player()
player1.name = input("Hey, there! Thank you for taking the time to sit down and take a nursing proficiency exam. May I ask you to please enter your name?\nName: ")
print(f"It's a pleasure to meet you, {player1.name}. This test has three sections. The first section is multiple choice and only one of the answers is correct. I hope that you will enjoy this section that is comprised of {len(questions)} questions.")
print("Section 1:\n")

for i in range(len(questions)):
    print(f"Question #{i + 1}:")
    print(f"{questions[i].get("Question")}\n")
    print(f"A: {questions[i].get("A")}\n")
    print(f"B: {questions[i].get("B")}\n")
    print(f"C: {questions[i].get("C")}\n")
    print(f"D: {questions[i].get("D")}\n")
    player_answer = input("Enter your answer: ")
    while player_answer.upper() not in questions[i]:
        player_answer = input("That is not a valid entry. Please enter an answer from A to D: ")
    if questions[i].get("Answer") == player_answer.upper():
        player1.score += 1
        player1.update_total_score()
        print("Correct!\n")
    else:
        print(f"The correct answer is {questions[i].get("Answer")}\n")

print(f"Good job on finishing the first section, {player1.name}! We are now entering section two of the exam.  This section has questions with multiple correct answers and there are {len(multi_answer_questions)} questions in total.")
print("Section 2:\n")


for i in range(len(multi_answer_questions)):
    print(f"Question #{i + 1}:")
    print(f"{multi_answer_questions[i].get("Question")}\n")
    for option, answer in multi_answer_questions[i]["Options"].items():
        print(f"{option}: {answer}\n")
    print("Please enter your answers seperated by a space (e.g. 'A B C')")
    player_answer = input("Your answer: ")
    answer_list = player_answer.upper().split()
    while not all(answer in multi_answer_questions[i]["Options"] for answer in answer_list):
        player_answer = input("Please enter a valid response:")
        player_answer = input("Your answer: ")
        answer_list = player_answer.upper().split()
    correct_answers_list = multi_answer_questions[i]["CorrectAnswers"]
    correct_answers = " ".join(correct_answers_list)
    if sorted(answer_list) == sorted(correct_answers_list):
        player1.score += 1
        player1.update_total_score()
        print("Correct!\n")
    else:
        print(f"The correct answer(s) are {correct_answers}\n")

print(f"We're done with section two! Let's start the third, and final, section of the exam. This is a fill-in-the-blank type section. There are only {len(fill_in_the_blank_questions)} questions in total.")
print("Section 3:\n")

question_number = 1
for question in fill_in_the_blank_questions:
    print(f"Question {question_number}:")
    print(question.get("Question") + "\n")
    question_number += 1
    player_answer = input("Your answer: ").strip().lower()
    if question.get("Special"):
        answers = player_answer.split()
        if len(answers) == 2 and all(a in [answer.lower() for answer in question["Answers"]] for a in answers):
            player1.score += 1
            player1.update_total_score()
            print("Correct!\n")
        else:
            print(f"The correct answers could include any two of: {question.get("Answers")}\n")
    else:
        if player_answer.lower() in question.get("Answers"):
            player1.score += 1
            player1.update_total_score()
            print("Correct!\n")   
        else:
            print(f"The correct answer is {question.get("Answers")}\n")

print(player1)