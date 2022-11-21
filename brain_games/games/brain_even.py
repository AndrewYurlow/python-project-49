#!/usr/bin/env python3
from brain_games.scripts.brain_games import main as greet_user
from brain_games.scripts import game_functions



def main():
    greet_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_functions.start(game_functions.get_random_number)
    

if __name__ == "__main__":
    main()
