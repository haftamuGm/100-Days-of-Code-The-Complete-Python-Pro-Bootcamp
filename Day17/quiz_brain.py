class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    def still_has_question(self):
        return len(self.question_list)>self.question_number

    def nextquestion(self):
        currentquestion=self.question_list[self.question_number]
        answer=input(f"Q{self.question_number }:{currentquestion.text}(True/False): ").lower()
        self.question_number += 1
        self.check_answer(answer,currentquestion.answer)

    def check_answer(self,user_ans,real_ans):
        if user_ans==real_ans.lower():
            self.score+=1
            print("You got it Right")
        else:
            print("That's Wrong")
        print(f"The Correct Answer was :{real_ans}")
        print(f"Your Current Score is :{self.score}/{self.question_number}")
        print('\n'*1)
