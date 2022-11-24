from brain_games.scripts.game_data import data
from brain_games.scripts import game_utils as gu


def start(get_expression, get_correct_answer):
    user_state = data['user_is_won']
    questions_amount = data['question_amount']
    name = data['user_name']
    while questions_amount > 0:
        expression = get_expression()
        gu.ask_question(expression)
        answer = gu.get_answer()
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
        print(f"Let's try again, {name}!")
