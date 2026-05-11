import random
from generator import generate_secret_number
from game_logic import get_clues

def main():
    print("LET'S PLAY THE GAME")
    secret_number = generate_secret_number()
    while True:      
        user_num = input()
        clues = get_clues(user_num, secret_number)
        if user_num == secret_number:
            print('Mamy to')   
            break
        else:
             print(clues)


main()

assert get_clues('666','123') == ['bajgle']