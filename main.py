import random

def generate_secret_number():
     secret_number = str(random.randint(100,999))
     if isinstance(secret_number, str):
          print(secret_number)
     return secret_number
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

def get_clues(user_num, secret_number):
        clues = []
        for index, number in enumerate(user_num):
            if number == secret_number[index]:
                clues.append('femi')
            elif number in secret_number:
                clues.append('piko')
        if clues == []:
             clues.append('bajgle')
        return clues
main()

assert get_clues('666','123') == ['bajgle']