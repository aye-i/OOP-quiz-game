from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question_dict in question_data:
    q_text = question_dict["text"]
    q_ans = question_dict["answer"]
    question_object = Question(q_text,q_ans)
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(quiz.final_score())