import sys
from data import data_exam
from question_model import Question
from quiz_brain import QuizBrain
question_bank=[]
for i in data_exam:
    ques=i['question']
    ans=i['correct_answer']
    ask_ans=Question(ques,ans)
    question_bank.append(ask_ans)
quiz=QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.nextquestion()
print("You've Completed The Quiz")
print(f"Your Final Score was :{quiz.score}/{quiz.question_number}")