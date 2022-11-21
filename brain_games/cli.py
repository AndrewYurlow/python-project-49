import prompt
from brain_games.scripts.game_states import states


def welcome_user():
    name = prompt.string('May I have your name? ')
    states['user_name'] = name
    print(f'Hello, {name}!')
