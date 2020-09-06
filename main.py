import random as rand
import time
import math
import threading as thread

print("")
print("Homework Practice --version 0.1.5")
print("Added FULL time trial mode")
print("")
print('')


def choose_state():
    print('> Do you 1. do a time trial?')
    print('> Or do you want 2. practice?')
    i = input('> ')
    numc = float(i)
    try:
        if numc == 2:
            print('Starting "Practice Mode"!')
            print('')
            start_practice()
        elif numc == 1:
            print('Starting the Time Trial setup!')
            print('')
            setup_time_trial()

    except ValueError:
        print('Please enter a number: 1 if you want to do a time trial...')
        print('Or 2 if you want to practice!')
        choose_state()


def start_practice():
    chance1 = rand.randint(1, 10)
    chance2 = rand.randint(1, 10)
    x = "x" if chance1 >= 5 else "a"
    y = "y" if chance2 >= 5 else "z"
    xValue = rand.randint(-10, 100)
    yValue = rand.randint(-10, 100)
    qc1 = rand.randint(1, 100)
    qc2 = rand.randint(1, 100)
    question_operator1 = "find the sum" if qc1 >= 50 else "find the difference"
    question_operator2 = f"find the Product of {x}, {y}" if qc2 >= 50 else "find the quotient"

    answer1 = xValue + yValue if qc1 >= 50 else xValue - yValue
    answer2 = xValue * yValue if qc2 >= 50 else xValue / yValue

    answer = answer1 if qc1 > qc2 else answer2

    question = input(f'> If {x} = {xValue}, and {y} = {yValue}, {question_operator1}: ') if qc1 > qc2 else input(f'> If {x} = {xValue}, and {y} = {yValue}, {question_operator2} (calculator allowed!): ')
    try:
        i = float(question)
        if i == answer:
            print("Correct!")
            print('')
            print('')
            start_practice()
        else:
            print("Incorrect!")
            print(f'answer was: {answer}')
            print('')
            print('')
            start_practice()
        if i == -0:
            print('going to menu!')
            choose_state()
    except ValueError:
        print("Syntax error!")
        print("")
        print("")
        start_practice()


seconds = None


def setup_time_trial():
    i = input(f"> How many seconds do you want to have? ")
    seconds = int(i)
    try:
        print('')
        print("Starting Time Trial")
        print('')
        print('')
        start_time_trial()
    except ValueError:
        print("Please Enter the Number of Seconds You Want...")
        print('')
        print('')
        setup_time_trial()


def start_time_trial():
    chance1 = rand.randint(1, 10)
    chance2 = rand.randint(1, 10)
    x = "x" if chance1 >= 5 else "a"
    y = "y" if chance2 >= 5 else "z"
    xValue = rand.randint(-10, 100)
    yValue = rand.randint(-10, 100)
    qc1 = rand.randint(1, 100)
    qc2 = rand.randint(1, 100)
    question_operator1 = "find the sum" if qc1 >= 50 else "find the difference"
    question_operator2 = f"find the Product of {x}, {y}" if qc2 >= 50 else "find the quotient"

    answer1 = xValue + yValue if qc1 >= 50 else xValue - yValue
    answer2 = xValue * yValue if qc2 >= 50 else xValue / yValue

    answer = answer1 if qc1 > qc2 else answer2

    question = input(f'> If {x} = {xValue}, and {y} = {yValue}, {question_operator1}: ') if qc1 > qc2 else input(f'> If {x} = {xValue}, and {y} = {yValue}, {question_operator2} (calculator allowed!): ')
    try:
        i = float(question)
        if i == answer:
            print("Correct!")
            print('')
            print('')
            start_time_trial()
        else:
            print("Incorrect!")
            print(f'answer was: {answer}')
            print('')
            print('')
            start_time_trial()
    except ValueError:
        print("Syntax error!")
        print("")
        print("")
        start_time_trial()

    timer = thread.Timer(seconds, end_trial)
    timer.start()
    if i == answer:
        timer.cancel()
        timer.start(seconds)
    else:
        timer.cancel()
        timer.start(seconds)


def end_trial():
    print(' ')
    print('Out of time! :( ')
    i = input('Would you like to 1. restart this program? Or 2. go to the menu? ')
    end_choice = int(i)
    try:
        if end_choice == 1:
            setup_time_trial()
        elif end_choice == 2:
            choose_state()
            print('')
            print("~~~~~~~~~~~~~~~~~~~~~~~~")
            print('')
        else:
            print('those were not options...')
            print('')
            print('')
            end_trial()

    except ValueError:
        print('please choose 1 if you would like to restart or 2 if you would like to go to the menu...')


choose_state()

