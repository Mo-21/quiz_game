from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize(width=320, height=600)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.q_text = self.canvas.create_text(150, 125, text=self.quiz.next_question(), font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.get_next_question)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file="false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.get_next_question)
        self.false_btn.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        new_q = self.quiz.next_question()
        self.canvas.itemconfig(self.q_text, text=new_q)
