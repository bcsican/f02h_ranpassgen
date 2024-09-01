import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "" .join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    
    password_length = int(input("Enter password length: "))
    if password_length < 12:
        print("Password length must be at least 12 characters. RUN SCRIPT AGAIN.")
    else:
        generated_password = generate_password(password_length)
        print("Generated password:", generated_password)
        