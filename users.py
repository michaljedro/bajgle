import json 

def load_users():
    with open('users.json') as user_file:
        users = json.load(user_file)
        return users



users = load_users()

def find_user_by_email(users,email):
    for user in users:
        if user['email'] == email:
            return user
    return None

user = find_user_by_email(users,"ciapka1805@wp.pl")

if user:
    print(user)
else:
    print('User not found')