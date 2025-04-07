from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')

class QuizInterface:

    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score : 0', bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=275, text="The first computer bug was formed by faulty wires.", fill='black', font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right_image = PhotoImage(file='./images/true.png')
        self.right_btn = Button(image=right_image, highlightthickness=0, command=self.right_btn_click)
        self.right_btn.grid(column=0, row=2)

        wrong_image = PhotoImage(file='./images/false.png')
        self.wrong_btn = Button(image=wrong_image, highlightthickness=0, command=self.wrong_btn_click)
        self.wrong_btn.grid(column=1, row=2)


        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score_label.config(text=f"Score : {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else :
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def right_btn_click(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_btn_click(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right : bool):
        bg_color = 'green' if is_right else 'red'
        self.canvas.config(bg=bg_color)
        self.window.after(1000, self.get_next_question)



