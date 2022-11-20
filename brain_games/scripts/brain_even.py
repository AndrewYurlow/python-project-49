#!/usr/bin/env python3
import prompt
from random import randint


def main():
    print("Welcome to the Brain Games!")
    start()


def start():
    user_is_won = False
    number_of_questions = 3
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while number_of_questions > 0:
        number = randint(1, 100)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        correct_answer = get_correct_answer(number)
        if (answer == correct_answer):
            print("Correct!")
            number_of_questions -= 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            break
    if number_of_questions == 0:
        user_is_won = True
    end_game(name, user_is_won)


def end_game(user_name, user_game_state):
    if user_game_state:
        print(f"Congratulations, {user_name}!")
    else:
        print(f"Let's try again, {user_name}")


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def get_correct_answer(num):
    if is_even(num):
        return "yes"
    else:
        return "no"


if __name__ == "__main__":
    main()
