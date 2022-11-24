#!/usr/bin/env python3
from brain_games.scripts.brain_games import main as greet_user
from brain_games.scripts.game_logic import start
from brain_games.scripts.game_utils import get_rand_num, is_given_number_prime


def main():
    greet_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    start(get_rand_num, is_given_number_prime)


if __name__ == "__main__":
    main()
