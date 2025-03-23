import random
import string
import sys


# Ask the user for the length of the password > 8
# divide it into 3 parts e.g. if he enters len=12 then divide it by 3 = 4
# each part must let the user enter allow the user to enter their own 4 letters, numbers, & puncs.
# form those chars randomly sort them & create a password out of them.
# It can further by creating a file and storing the password. Also encrypting the file for safety

def _GenerateWithUserChars(length):
    c_len = int(length / 3)
    len_rem = length % 3

    # methods can be used
    chars = input(f"\nEnter {c_len + len_rem} alphabets (letters only): ")
    if chars.isalpha() and len(chars) == (c_len + len_rem):
        _nums = input(f"Enter {c_len} numbers (digits only): ")
        if _nums.isdigit() and len(_nums) == c_len:
            _punc = input(f"Enter {c_len} punctuations only: ")
            if _punc in string.punctuation and len(_punc) == c_len:
                combination = _nums + _punc + chars
                password = ''.join(random.sample(combination, length))
                print(f"\nPassword => {password}\n")
            else:
                print(f"\nTry again and enter punctuations only with a length of {c_len}.\n")
        else:
            print(f"\nTry again and enter digits only with a length of {c_len}.\n")
    else:
        print(f"\nTry again and enter alphabets only! with a length of {c_len + len_rem}.\n")


def generate_password(_length):
    _chars = string.ascii_letters + string.digits + string.punctuation

    # password = ''.join(random.choice(_chars) for _ in range(length))
    password = ''.join(random.sample(_chars, _length))  # Solution 2
    print(f"\nPassword => {password}\n")


if __name__ == "__main__":
    length = input("Enter the length of the password ( >= 8): ")

    if length.isnumeric() and int(length) >= 8:
        length = int(length)

        option = input("Do you want to generate a password with your own set of characters(Y/N)? ").upper()

        if option == "Y":
            _GenerateWithUserChars(length)
        elif option == "N":
            generate_password(length)
        else:
            print("\nWrong input, try again!\n")

    else:
        print("\nThe value must be numeric and >= 8.\n")

    sys.exit()







