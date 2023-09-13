class QuizBrain:
    def __init__(self, question_list):
        self.question_num = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        curr_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}) {curr_question.text} --> True or False?\n-->").lower()
        self.check_answer(user_answer, curr_question.answer)
        # for q_obj in self.question_list:
        #     user_answer = input(f"Q.{self.question_num+1}) {q_obj.text} --> True or False?\n-->").lower()
        #     if user_answer != q_obj.answer.lower():
        #         print(f"Oops! Incorrect!\t\tScore:{self.score}")
        #     elif user_answer == q_obj.answer.lower():
        #         self.score += 1
        #         print(f"Correct!\t\tScore:{self.score}")
        #     self.question_num+=1

    def check_answer(self, answer_by_user, actual_answer):
        if answer_by_user.lower() == actual_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
        print(f"Correct answer is {actual_answer}!")
        print(f"Current Score is {self.score}/{self.question_num}\n")

    def final_score(self):
        return f"You've completed the Quiz!\nFinal Score is {self.score}/{self.question_num}\n"
