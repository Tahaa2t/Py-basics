class QuizBrain:
    def __init__(self,question_list):
        self.question_list = question_list
        self.question_number = 0
        self.correct = 0


    def check_correct(self,ans,correct):
        return ans.lower() == correct.lower()


    def next_q(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        check = input(f"Q.{self.question_number}: {current_q.text} (True/False): ")
        if self.check_correct(check,current_q.answer):
            print("Correct answer 😁",end=" ")
            self.correct +=1
        else:
            print("Incorrect answer 😬",end=" ")
        
        self.display_score()

    def still_has_question(self):
        return self.question_number < len(self.question_list)


    
    def display_score(self):
        print(f"Your score is: {self.correct}/{self.question_number}\n\n")
