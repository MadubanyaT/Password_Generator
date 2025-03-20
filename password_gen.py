import random
import string


def generate_password(length=3):
    _chars = string.ascii_letters + string.digits + string.punctuation

    # password = ''.join(random.choice(_chars) for _ in range(length))
    password = ''.join(random.sample(_chars, length))  #Solution 2
    print(password)

generate_password()

