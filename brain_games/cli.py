import prompt
from brain_games.scripts.game_data import data


def welcome_user():
    name = prompt.string('May I have your name? ')
    data['user_name'] = name
    print(f'Hello, {name}!')
