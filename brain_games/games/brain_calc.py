#!/usr/bin/env python3
from brain_games.scripts.brain_games import main as greet_user
from brain_games.scripts.game_logic import start
from brain_games.scripts.game_utils import get_rand_expr, get_result_calc


def main():
    greet_user()
    print('What is the result of the expression?')
    start(get_rand_expr, get_result_calc)


if __name__ == "__main__":
    main()
