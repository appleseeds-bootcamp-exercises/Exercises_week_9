import random
import operator

OPERATORS = {'-': operator.sub, '+': operator.add, '*': operator.mul, '/': operator.truediv}


def generate_math_problem():
    first_operand = random.randint(1, 101)
    second_operand = random.randint(1, 101)
    chosen_operator = random.choice(list(OPERATORS))
    answer = round(OPERATORS.get(chosen_operator)(first_operand, second_operand),2)
    return {
        "question": f'{first_operand} {chosen_operator} {second_operand} = ',
        "correct_answer": answer
    }


def is_a_no(s):
    if any([s == "no", s == "No", s == "n", s == 'N']):
        return True
    return False


def is_a_yes(s):
    if any([s == "yes", s == "Yes", s == "y", s == 'Y']):
        return True
    return False


correct_answers = 0
wrong_answers = []
print("Hello and welcome to our math game")
print(
    "You will be required to answer basic math problems. I hope you are ready")
will_more_questions = True
while will_more_questions:
    problem = generate_math_problem()
    is_a_number = True
    answer = input(problem["question"])
    try:
        answer_as_float = float(answer)
    except ValueError:
        is_a_number = False
    if is_a_number and answer_as_float == problem['correct_answer']:
        print("Wow, impressive!")
        correct_answers += 1
    else:
        print("Sorry mate :/")
        wrong_answers.append(f'{problem["question"]} {answer} ({str(problem["correct_answer"])})')
    did_answer = False
    while not did_answer:
        will_another = input("Would you like to try another problem?  ")
        if is_a_no(will_another):
            did_answer = True
            will_more_questions = False
        elif is_a_yes(will_another):
            did_answer = True
        else:
            print("Sorry didn't catch your reply")

print("Hope you had fun playing")
print(
    f'Your score is: {100* correct_answers/(correct_answers + len(wrong_answers))}%'
)
print("Questions you answered wrong: ")
for a in wrong_answers:
    print(a)
print("Thank you")