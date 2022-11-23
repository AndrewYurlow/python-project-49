#!/usr/bin/env python3
from brain_games.scripts.brain_games import main as greet_user
from brain_games.scripts.game_logic import start
from brain_games.scripts.game_utils import get_rand_num, get_correct_answer_br_even


def main():
    greet_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    start(get_rand_num, get_correct_answer_br_even)


if __name__ == "__main__":
    main()
