import requests


class API:

    def __init__(self, params):
        self.url = "https://opentdb.com/api.php"
        self.params = params

    def get_questions(self):
        response = requests.get("https://opentdb.com/api.php", params=self.params)
        questions = response.json()
        return questions, response.status_code
