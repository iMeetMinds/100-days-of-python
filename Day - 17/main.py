from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for n in question_data:
    question_bank.append(Question(n['text'], n['answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_no}")