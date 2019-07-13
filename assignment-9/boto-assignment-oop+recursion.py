import random
from utils import OPERATORS, is_a_no, is_a_yes


class Game:
    def __init__(self):
        self.unsolved_problems = []
        self.num_correct_answers = 0

    def play(self):
        print("Hello and welcome to our math game")
        print(
            "You will be required to answer basic math problems. I hope you are ready"
        )
        self.ask_math_question()
        print("Hope you had fun playing!!")
        success_rate = int(100 * self.num_correct_answers /
                           (self.num_correct_answers + len(self.unsolved_problems)))
        print(
            f'Your score is: {success_rate}%'
        )
        if len(self.unsolved_problems) > 0:
            print("Questions you answered wrong: ")
            for a in self.unsolved_problems:
                print(a)
        print("See you next time!")

    def generate_math_problem(self):
        first_operand = random.randint(1, 101)
        second_operand = random.randint(1, 101)
        chosen_operator_symbol, chosen_operator = random.choice(
            list(OPERATORS.items()))
        answer = round(
            chosen_operator(first_operand, second_operand), 2)
        return {
            "question":
            f'{first_operand} {chosen_operator_symbol} {second_operand} = ',
            "correct_answer": answer
        }

    def ask_math_question(self):
        problem = self.generate_math_problem()
        print(problem["question"])
        user_answer = self.accept_math_answer()
        if user_answer == problem['correct_answer']:
            print(random.choice(
                ["Excellent! ", "Wow, impressive!", "You're good!"]))
            self.num_correct_answers += 1
        else:
            print(random.choice(
                ["Sorry mate :/ ", "You can do better!", "Try harder next time, ok?"]))
            self.unsolved_problems.append(
                f'{problem["question"]} {user_answer} ({str(problem["correct_answer"])})'
            )
        if self.will_another_problem():
            self.ask_math_question()

    def accept_math_answer(self):
        try:
            return float(input())
        except ValueError:
            print("Sorry that was not a valid number, please try again.")
            return self.accept_math_answer()

    def will_another_problem(self):
        will_another = input("Would you like to try another problem?  ")
        if is_a_no(will_another):
            return False
        if is_a_yes(will_another):
            return True
        print("Sorry didn't catch your reply")
        return self.will_another_problem()


Game().play()
