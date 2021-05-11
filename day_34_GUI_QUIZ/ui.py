from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label_score = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.label_score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.q_text = self.canvas.create_text(150, 125, text='Question here', fill=THEME_COLOR, width=280,
                                              font=('Arial', 20, 'italic'))
        self.canvas.grid(pady=50, row=1, column=0, columnspan=2)

        image_true = PhotoImage(file='images/true.png')
        image_false = PhotoImage(file='images/false.png')
        self.btn_true = Button(image=image_true, bg=THEME_COLOR, activebackground=THEME_COLOR, highlightthickness=0,
                               bd=0, command=self.ans_true)
        self.btn_false = Button(image=image_false, bg=THEME_COLOR, activebackground=THEME_COLOR, highlightthickness=0,
                                bd=0, command=self.ans_false)
        self.btn_true.grid(row=2, column=0)
        self.btn_false.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.label_score.config(text=f'Score: {self.quiz.score}/{self.quiz.question_number}')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
        else:
            self.canvas.itemconfig(self.q_text, text="You've reached the end of this quiz.")
            self.btn_true.config(state='disabled')
            self.btn_false.config(state='disabled')

    def ans_true(self):
        self.feedback(self.quiz.check_answer('True'))

    def ans_false(self):
        self.feedback(self.quiz.check_answer('False'))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(600, self.get_next_question)
