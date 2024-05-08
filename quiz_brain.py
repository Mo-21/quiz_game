class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.number_of_questions = len(self.question_list)
        self.score = 0

    def next_question(self):
        while self.question_number < self.number_of_questions:
            current_question = self.question_list[self.question_number]
            answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)  ")
            self.check_answer(answer, current_question.answer)
            self.question_number += 1
        self.final_result()

    def check_answer(self, user_answer, true_answer):
        if user_answer == true_answer:
            print("Correct answer ^_^")
            self.score += 1
            print(f"\nCurrent Score: {self.score}")
        else:
            print("Wrong :(")
            print(f"\nCurrent Score: {self.score}")

    def final_result(self):
        print("\nYou have completed the quiz")
        print(f"Your final result is {self.score}, you got {self.score}/{self.number_of_questions}")