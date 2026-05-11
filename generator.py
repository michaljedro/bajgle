def generate_secret_number():
     secret_number = str(random.randint(100,999))
     if isinstance(secret_number, str):
          print(secret_number)
     return secret_number
