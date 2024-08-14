import random

class Question():
    def __init__(self, question, correct_answer, incorrect_answers) -> None:
        self.question = question
        self.correct_answer = correct_answer
        incorrect_answers.append(correct_answer)
        random.shuffle(incorrect_answers)
        self.answers = incorrect_answers
        print()
        