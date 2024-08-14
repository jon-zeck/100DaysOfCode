from TriviaBrain import TriviaBrain
from Question import Question
from Data import Data

if __name__ == "__main__":
    data = Data()

    # data.set_quiz_parameters()
    json_questions = data.setup_questions()

    questions = []
    for question_obj in json_questions:
        question = question_obj["question"]
        correct_answer = question_obj["correct_answer"]
        answers = question_obj["incorrect_answers"]
        questions.append(Question(question, correct_answer, answers))

    trivia = TriviaBrain(questions)

    while trivia.still_has_question():
        trivia.ask_question()
        trivia.evaluate_answer()

''' 
    Requirements:
        1. Keep track of score
        2. Generate questions via URL link.
        3. Show the user a question
        4. check if the answer is correct.

        One class could be the question card generator.
        Another could be a class that generates the questions & keeps track of score.
'''