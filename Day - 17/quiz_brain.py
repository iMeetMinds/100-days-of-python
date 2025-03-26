class QuizBrain:

    def __init__(self, question_bank):
        self.question_no = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no].question
        current_answer = self.question_list[self.question_no].answer
        self.question_no += 1
        user_ans = input(f"Q.{self.question_no}: {current_question} (True/False): ").lower()
        self.check_answer(user_ans, current_answer)

    def check_answer(self, user_ans, current_answer):
        if user_ans == current_answer.lower():
            self.score += 1
            print("You got it right!!")
        else:
            print("That's wrong!!")

        print(f"The correct answer was {current_answer}.")
        print(f"Your current score is {self.score}/{self.question_no}.")
        print("\n")
