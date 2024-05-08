from question_model import Question
from quiz_brain import QuizBrain
from api_service import API
import json
import html

parameters = {"amount": 10, "type": "boolean"}
api = API(parameters)
questions, status_code = api.get_questions()

if status_code == 200:
    with open("questions.json", mode="w") as file:
        json.dump(questions["results"], file, indent=4)

    questions_bank = [Question(html.unescape(q["question"]), q["correct_answer"]) for q in questions["results"]]

    quiz = QuizBrain(questions_bank)
    quiz.next_question()
else:
    raise Exception(status_code)

