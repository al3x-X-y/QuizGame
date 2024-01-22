# TODO: asking q
# TODO: checking if ans is correct
# TODO: checking if we're at the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.current_question = None
        self.next_question()

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if self.still_has_questions():
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            print(f"Catergory: {self.current_question.catagory} \nDifficulty: {self.current_question.difficulty} \nType: {self.current_question.type}")
            user_ans = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
            self.check_answer(user_ans)
    def check_answer(self, user_ans):
        correct_ans = self.current_question.answer
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        elif user_ans.lower() == "exit":
            print("You have exited the quiz.")
            print(f"Your final score was: {self.score}/{self.question_number}")
            exit()
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_ans}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")