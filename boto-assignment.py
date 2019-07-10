def generate_math_problem():
    return {"question": "q?", "correct_answer": 5}


correct_answers = 0
wrong_answers = []
print("Hello and welcome to our math game")
print(
    "You will be required to answer basic math problems. I hope you are ready")

while True:
    problem = generate_math_problem()
    answer = int(input(problem["question"]))
    if answer == problem['correct_answer']:
        print("Wow, impressive!")
        correct_answers += 1
    else:
        print("Sorry mate :/")
        wrong_answers += problem['question'] + str(problem['correct_answer'])
    will_another = input("Would you like to try another problem?")
    if (will_another == "no"):
        break
print("Hope you had fun playing")
print(f'Your score is: {100-(100* len(wrong_answers)/correct_answers)}%')
print("Thank you")