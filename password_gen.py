import random
import string
import sys


# Ask the user for the length of the password > 8
# divide it into 3 parts e.g. if he enters len=12 then divide it by 3 = 4
# each part must let the user enter allow the user to enter their own 4 letters, numbers, & puncs.
# form those chars randomly sort them & create a password out of them.
# It can further by creating a file and storing the password. Also encrypting the file for safety

def generateWithUserChars(length, loop):
    c_len = int(length / 3)
    len_rem = length % 3
    i = 1

    # methods can be used
    chars = input(f"\nEnter {c_len + len_rem} alphabets (letters only): ")
    if chars.isalpha() and len(chars) == (c_len + len_rem):
        _nums = input(f"Enter {c_len} numbers (digits only): ")
        if _nums.isdigit() and len(_nums) == c_len:
            _punc = input(f"Enter {c_len} punctuations only: ")
            if checkPunctuations(_punc) and len(_punc) == c_len:
                combination = _nums + _punc + chars
                while i <= loop:
                    # password = ''.join(random.choice(combination) for _ in range(length))
                    password = ''.join(random.sample(combination, length))
                    print(f"\nPassword {i} => {password}")
                    i += 1
            else:
                print(f"\nTry again and enter punctuations only with a length of {c_len}.\n")
        else:
            print(f"\nTry again and enter digits only with a length of {c_len}.\n")
    else:
        print(f"\nTry again and enter alphabets only! with a length of {c_len + len_rem}.\n")

    print()


def generate_Password(_length, loop):
    _chars = string.ascii_letters + string.digits + string.punctuation
    i = 1
    while i <= loop:
        # password = ''.join(random.choice(_chars) for _ in range(length))
        password = ''.join(random.sample(_chars, _length))  # Solution 2
        print(f"\nPassword {i} => {password}")
        i += 1

    print()

def checkPunctuations(punc):
    finalP = ""

    for p1 in punc:
        for p2 in string.punctuation:
            if p1 == p2:
                finalP += p2
                break

    if punc == finalP:
        return True

    return False


if __name__ == "__main__":
    length = input("Enter the length of the password ( >= 8): ")

    if length.isnumeric() and int(length) >= 8:
        length = int(length)

        option = input("Do you want to generate a password with your own set of characters(Y/N, y/n)? ").upper()
        numP = input("How many password(s) do you want to generate ( >= 1)? ")

        if numP.isnumeric() and int(numP) >= 1:
            if option == "Y":
                generateWithUserChars(length, int(numP))
            elif option == "N":
                generate_Password(length, int(numP))
            else:
                print("\nWrong input, try again! (Y/N, y/n)\n")
        else:
            print("\nWrong input, digits only and must be >= 1 are allowed.\n")

    else:
        print("\nThe value must be numeric and >= 8.\n")

    sys.exit()
