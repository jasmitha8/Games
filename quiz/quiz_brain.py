class Brain:
    def __init__(self, question):
        self.q_no = 0
        self.q_list = question
        self.score = 0

    def next_question(self):
        current_ques = self.q_list[self.q_no]
        self.q_no += 1
        print(" ")
        answer = input(f"Q.{self.q_no}: {current_ques.text} (True/False)")
        self.check(answer, current_ques.answer)

    def still_has_question(self):
        return self.q_no < len(self.q_list)

    def check(self, answer, soln):
        if answer.lower() == soln.lower():
            self.score += 1
            print(f"Correct! Score: {self.score}/{len(self.q_list)}")
        else:
            self.q_no = len(self.q_list)
            print(f"Wrong answer.")
            self.still_has_question()

