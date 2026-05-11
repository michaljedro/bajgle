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