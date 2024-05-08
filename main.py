from api_service import API
from quiz_brain import QuizBrain
from question_model import Question
import html
import json
from ui import QuizInterface

parameters = {"amount": 10, "type": "boolean"}
api = API(parameters)
questions, status_code = api.get_questions()

if status_code == 200:
    with open("questions.json", mode="w") as file:
        json.dump(questions["results"], file, indent=4)

    questions_bank = [Question(html.unescape(q["question"]), q["correct_answer"]) for q in questions["results"]]

    quiz = QuizBrain(questions_bank)
    ui = QuizInterface(quiz)
else:
    raise Exception(status_code)

