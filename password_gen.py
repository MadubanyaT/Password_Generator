import random
import string
import sys
from Encoding import Cryptography

encoding = Cryptography()


def banner():
    print("""
 _______    ______    ______    ______         ________  __    __   ______  
/       \  /      \  /      \  /      \       /        |/  \  /  | /      \ 
$$$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |      $$$$$$$$/ $$  \ $$ |/$$$$$$  |
$$ |__$$ |$$ |__$$ |$$ \__$$/ $$ \__$$/       $$ |__    $$$  \$$ |$$ |  $$/ 
$$    $$/ $$    $$ |$$      \ $$      \       $$    |   $$$$  $$ |$$ |      
$$$$$$$/  $$$$$$$$ | $$$$$$  | $$$$$$  |      $$$$$/    $$ $$ $$ |$$ |   __ 
$$ |      $$ |  $$ |/  \__$$ |/  \__$$ |      $$ |_____ $$ |$$$$ |$$ \__/  |
$$ |      $$ |  $$ |$$    $$/ $$    $$/______ $$       |$$ | $$$ |$$    $$/ 
$$/       $$/   $$/  $$$$$$/   $$$$$$//      |$$$$$$$$/ $$/   $$/  $$$$$$/  
                                      $$$$$$/                                                                                                                                                                                                                                                                                                                                
    """)


# Working with Passwords
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
                    print(f"\nPassword {i} => {password}", end='')
                    i += 1

                print('\n[+] You can copy a password to save and encrypt.')
                return True
            else:
                print(f"\n[-] Try again and enter punctuations only with a length of {c_len}. NB: No currency symbols!")
        else:
            print(f"\n[-] Try again and enter digits only with a length of {c_len}.")
    else:
        print(f"\n[-] Try again and enter alphabets only! with a length of {c_len + len_rem}.")

    return False


def generateRanPassword(_length, loop):
    _chars = string.ascii_letters + string.digits + string.punctuation
    i = 1
    while i <= loop:
        # password = ''.join(random.choice(_chars) for _ in range(length))
        password = ''.join(random.sample(_chars, _length))  # Solution 2
        print(f"Password {i} => {password}")
        i += 1

    print('\n[+] You can copy a password to save and encrypt.')
    return True


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


# Cryptography
def encryptPassword():
    password = input('''Enter the password you've copied: ''')
    webName = input('Enter the website for the password (optional): ')
    userName = input('Enter the associated username for the password (optional): ')

    if password != '':
        encoding.saveThenEncrypt(password, webName, userName)
        print('\n[-] ' + encoding.info)
    else:
        print('[-] No password was provided, try again!')


def decryptPassword():
    encryptedfile = input('\nEnter the filename/path of the encrypted file: ')
    key = input('Enter the encryption key: ')

    if encryptedfile == '' and key == '':
        print('[-] No input on the encrypted filename or key, try again!')
    else:
        k = bytes(key, 'utf-8')
        encoding.Decrypt(encryptedfile, k)
        if encoding.info != '':
            print('\n[+]' + encoding.info)


# main method
if __name__ == "__main__":
    banner()
    # Ask the user if they want to de
    fOption = input('A) Generate and encrypt a password.\nB) Decrypt a file.\nSelect an option (A/B): ').upper()

    if fOption == 'A':
        b = False
        length = input("\nEnter the length of the password ( >= 8): ")

        if length.isnumeric() and int(length) >= 8:
            length = int(length)

            numP = input("\nEnter number of password(s) you want to generate ( >= 1): ")

            if numP.isnumeric() and int(numP) >= 1:
                option = input("\nGenerate a password with your own set of characters(Y/N, y/n): ").upper()
                if option == "Y":
                    b = generateWithUserChars(length, int(numP))
                elif option == "N":
                    b = generateRanPassword(length, int(numP))
                else:
                    print("\n[-] Wrong input, try again! (Y/N)")
            else:
                print("\n[-] Wrong input, digits only and must be >= 1")
        else:
            print("\n[-] The value must be numeric and >= 8.")

        if b:
            cOption = input("\nSave and encrypt a password (Y/N): ").upper()

            if cOption == 'Y' and b:
                encryptPassword()

    elif fOption == 'B':
        decryptPassword()
    else:
        print('\n[-] Wrong option, try again')

    print('\n[+] Thanks for using the program)')
    sys.exit()
