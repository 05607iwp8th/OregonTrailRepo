import random as rand
import math

print("")
print("Homework Practice --version 0.1.3")
print("Fixed ALL errors! Works like a well oiled machine! :]")
print("")

def start():
    chance1 = rand.randint(1, 10)
    chance2 = rand.randint(1, 10)
    x = "x" if chance1 >= 5 else "a"
    y = "y" if chance2 >= 5 else "z"
    xValue = rand.randint(-10, 100)
    yValue = rand.randint(-10, 100)
    qc1 = rand.randint(1, 100)
    qc2 = rand.randint(1, 100)
    print(f'SERVER_CHECK({qc1, qc2})')
    print("")
    question_operator1 = "find the sum" if qc1 >= 50 else "find the difference"
    question_operator2 = f"find the Product of {x}, {y}" if qc2 >= 50 else "find the quotient"

    answer1 = xValue + yValue if qc1 >= 50 else xValue - yValue
    answer2 = xValue * yValue if qc2 >= 50 else xValue / yValue

    answer = answer1 if qc1 > qc2 else answer2

    question = input(f'If {x} = {xValue}, and {y} = {yValue}, {question_operator1}: ') if qc1 > qc2 else input(f'If {x} = {xValue}, and {y} = {yValue}, {question_operator2} (calculator allowed!): ')
    try:
        i = int(question)
        if i == answer:
            print("Correct!")
            print('')
            start()
        else:
            print("Incorrect!")
            print(f'answer was: {answer}')
            print('')
            start()
    except ValueError:
        print("Syntax error!")
        print("")
        start()


start()


