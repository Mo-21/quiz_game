from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize(width=320, height=600)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.create_text(150, 125, text="Hello World", font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file="false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0)
        self.false_btn.grid(row=2, column=1)

        self.window.mainloop()
