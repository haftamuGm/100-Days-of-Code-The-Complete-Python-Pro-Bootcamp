THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class Quizzinterface():
    def __init__(self,quizz_brain:QuizBrain,):
        self.quiz=quizz_brain
        self.window=Tk()
        self.label=Label(text=f"score: 0",font=("arizial",14,"bold"),fg="white",bg=THEME_COLOR)
        self.label.grid(row=0,column=1)
        self.label.config(pady=5,padx=5)
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas=Canvas(width=300,height=250)
        self.question=self.canvas.create_text(150,120,width=280,text="Here it is The 'True' or'False' Question",font=("arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        right=PhotoImage(file="images/true.png")
        left=PhotoImage(file="images/false.png")
        self.rightbuttom=Button(image=right,command=self.true_pressed)
        self.rightbuttom.grid(row=2, column=0)
        self.leftbuttom=Button(image=left,command=self.false_pressed)
        self.leftbuttom.grid(row=2, column=1)
        self.get_next()
        self.window.mainloop()
    def get_next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.label.config(text=f"score :{self.quiz.score}")
            text=self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=text)


        else:
            self.canvas.itemconfig(self.question,text="You've Reach The End Of Question")
            self.rightbuttom.config(state="disabled")
            self.leftbuttom.config(state="disabled")
    def true_pressed(self):
        is_true=self.quiz.check_answer("True")
        self.feedback(is_true)
    def false_pressed(self):
        is_true=self.quiz.check_answer("False")
        self.feedback(is_true)

    def feedback(self,is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next)







