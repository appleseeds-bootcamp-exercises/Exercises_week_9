import random
import operator

OPERATORS = {
    '-': operator.sub,
    '+': operator.add,
    '*': operator.mul,
    '/': operator.truediv
}


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
        print("Hope you had fun playing")
        print(
            f'Your score is: {int(100* self.num_correct_answers/(self.num_correct_answers + len(self.unsolved_problems)))}%'
        )
        print("Questions you answered wrong: ")
        for a in self.unsolved_problems:
            print(a)
        print("Thank you")

    def generate_math_problem(self):
        first_operand = random.randint(1, 101)
        second_operand = random.randint(1, 101)
        chosen_operator = random.choice(list(OPERATORS))
        answer = round(
            OPERATORS.get(chosen_operator)(first_operand, second_operand), 2)
        return {
            "question":
            f'{first_operand} {chosen_operator} {second_operand} = ',
            "correct_answer": answer
        }

    def is_a_no(self, s):
        if any([s == "no", s == "No", s == "n", s == 'N']):
            return True
        return False

    def is_a_yes(self, s):
        if any([s == "yes", s == "Yes", s == "y", s == 'Y']):
            return True
        return False

    def ask_math_question(self):
        problem = self.generate_math_problem()
        is_a_number = True
        answer = input(problem["question"])
        try:
            answer_as_float = float(answer)
        except ValueError:
            is_a_number = False
        if is_a_number and answer_as_float == problem['correct_answer']:
            print("Wow, impressive!")
            self.num_correct_answers += 1
        else:
            print("Sorry mate :/")
            self.unsolved_problems.append(
                f'{problem["question"]} {answer} ({str(problem["correct_answer"])})'
            )
        if self.will_another_problem():
            self.ask_math_question()

    def will_another_problem(self):
        will_another = input("Would you like to try another problem?  ")
        if self.is_a_no(will_another):
            return False
        elif self.is_a_yes(will_another):
            return True
        else:
            print("Sorry didn't catch your reply")
            self.will_another_problem()


Game().play()