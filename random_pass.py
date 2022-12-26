import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password


input_length = int(input("Enter password length: "))
password = generate_password(input_length)
print(f"Generated password: {password}")
