''' Set up questions by querying opentdb API to retrieve a varibale number of questions with custom difficulty.'''
import json
import requests

class Data():
    def __init__(self) -> None:
        self.difficulty = "hard"
        self.questions_amount = 10
    
    def set_quiz_parameters(self):
        while True:
            self.difficulty = input("Select quiz difficulty: 'Easy', 'Medium' or 'Hard': ").lower()
            if self.difficulty == "easy" or self.difficulty == "medium" or self.difficulty == "hard":
                break
            print("Invalid input, try again.")
        while True:
            try:
                self.questions_amount = int(input("How many questions would you like: "))
                if self.questions_amount > 0:
                    break
                print("Invalid input, try again")
            except:
                print("It seems your input was not an number, try again.")

    def setup_questions(self):
        byte_content = self.retrieve_questions_byte_format()
        json_questions = self.convert_byte_to_json(byte_content)
        return json_questions

    def retrieve_questions_byte_format(self):
        api_url = f"https://opentdb.com/api.php?amount={self.questions_amount}&difficulty={self.difficulty}"
        response = requests.get(api_url)
        try:
            return response.content
        except:
            print("Failed to retrieve questions with status code: {response.status_code}")
            exit()

    def convert_byte_to_json(self, byte_content):
        json_content = byte_content.decode('utf8')
        content = json.loads(json_content)
        try:
            return content["results"]
        except:
            print(f"Failed to extract questions from json object. response_code = {content["response_code"]}")