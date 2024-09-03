import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

length = int(input("Enter password length: "))
print(f"Generated Password: {generate_password(length)}")
