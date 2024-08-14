''' This class asks questions, evaluates answers and keeps track of the user score '''

class TriviaBrain():
    def __init__(self, questions) -> None:
        self.score = 0
        self.questions = questions
        self.questions_asked = 0
    
    def ask_question(self):
        try:
            self.question = self.questions.pop()
            print(f"Question: {self.question.question}")
            print(f"Answers: {self.question.answers}")
            self.answer = input("What is your answer: ")
            self.questions_asked += 1
        except:
            print("It seems there are no more questions available...")

    def evaluate_answer(self):
        if self.answer.lower() == self.question.correct_answer.lower():
            self.score += 1
            print(f"Correct! Well done, your score is {self.print_score()}")
        else:
            print(f"Incorrect :( The correct answer is: {self.question.correct_answer}.")
            print(f"Your score is: {self.print_score()}")

    def print_score(self):
        return f"Your current score is: {self.score}/{self.questions_asked}"

    def still_has_question(self):
        if self.questions:
            return True
        return False
