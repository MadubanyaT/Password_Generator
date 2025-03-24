import struct

from cryptography.fernet import Fernet


# This class should not output anything, but write to files.
# The class can receive name of the website for password (but optional)
# Must have to encrypt, decrypt, createKey methods
# It can update the user if the key is created

class Encoding:

    def __init__(self):
        self.__websiteName__ = "Unknown Website"
        self.__userName__ = "Unknown Username"
        self.__secretKey__ = ""
        self.__info__ = ""

    def Encrypt(self, _webName, _userName, _password, _filename):
        key = __generateKey__(self)

        fernet = Fernet(key)

        file = open(_filename, '')


def __generateKey__(self):
    key = Fernet.generate_key()

    try:
        filekey = open('filekey.key', 'wb')
        filekey.write(key)
    except:
        raise Exception('Failed to write to the generated key.')

    filekey.close()
    self.__info__ += "The key has been generated and saved in the 'filekey.key' file."
    return key
