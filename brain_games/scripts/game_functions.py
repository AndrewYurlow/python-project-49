import prompt
from random import randint
from brain_games.scripts.game_states import states


def ask_question(statement):
    print(f"Question: {statement}")


def get_answer():
    answer = prompt.string("Your answer: ")
    return answer


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


def get_random_number():
    return randint(1, 100)


def start(get_expression):
    user_state = states['user_is_won']
    questions_amount = states['question_amount']
    name = states['user_name']
    while questions_amount > 0:
        expression = get_expression()
        ask_question(expression)
        answer = get_answer()
        correct_answer = get_correct_answer(expression)
        if (answer == correct_answer):
            print("Correct!")
            questions_amount -= 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            break
    if questions_amount == 0:
        user_state = True
    end_game(name, user_state)


def end_game(name, user_game_state):
    if user_game_state:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}")