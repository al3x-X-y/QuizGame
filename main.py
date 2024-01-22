from question_model import question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for i in question_data:
    question_text = i["question"]
    question_answer = i["correct_answer"]
    question_type = i["type"]
    question_difficulty = i["difficulty"]
    question_catagory = i["category"]
    new_question = question(question_text, question_answer, question_type, question_catagory, question_difficulty)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
