#!/usr/bin/env python3
from brain_games.scripts.brain_games import main as greet_user
from brain_games.scripts.game_logic import start
from brain_games.scripts.game_utils import get_progression, get_hidden_number


def main():
    greet_user()
    print('What number is missing in the progression?')
    start(get_progression, get_hidden_number)


if __name__ == "__main__":
    main()
