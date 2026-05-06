secret_number = '123'
def main():
    print("LET'S PLAY THE GAME")
    while True:      
        user_num = input()
        clues = []
        for index, number in enumerate(user_num):
            if number == secret_number[index]:
                print(f'{number} and {secret_number[index]}')
                print('remis')
        if user_num == secret_number:
            print('Mamy to')   
            break
        else:
            print("Źle")
main()

