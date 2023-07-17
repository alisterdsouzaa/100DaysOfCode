from question_model import *
from data import *
from quiz_brain import *

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_obj = Question(text=question_text, answer=question_answer)
    question_bank.append(question_obj)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_method()

