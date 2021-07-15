from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []


for qs in question_data:
    ask = Question(qs["text"],qs["answer"])
    question_bank.append(ask)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_q()

print(f"you've completed the quiz!!, your final score is: {quiz.correct}/{quiz.question_number}")