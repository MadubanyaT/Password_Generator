import struct

import cryptography
import os

from cryptography.exceptions import InvalidSignature
from cryptography.fernet import Fernet, InvalidToken


# This class should not output anything, but write to files.
# The class can receive name of the website for password (but optional)
# Must have to encrypt, decrypt, createKey methods
# It can update the user if the key is created


class Encoding:
    def __init__(self, Key=None):
        self.__secretKey__ = Key or Fernet.generate_key()
        self.__cipher__ = Fernet(self.__secretKey__)
        self.__info__ = ""

    def Encrypt(self, _filename, _password, _webName="Unknown Website", _userName="Unknown Username", ):
        self.__saveKey__()
        # fernet = Fernet(self.__secretKey__)

        try:
            # file_w = open(_filename, 'a')
            text = ('Website name: ' + _webName + ', Username: '
                    + _userName + ', Password: ' + _password + '\n').encode('utf-8')

            encrypted = self.__cipher__.encrypt(text)

            print(encrypted)
            file_w = open(_filename, 'wb')
            file_w.write(encrypted)
        except:
            raise Exception('An error occurred.')

        file_w.close()
        print(self.__secretKey__)

    def Decrypt(self, _encryptedFilename, _decryptedFilename):
        try:
            file_r = open(_encryptedFilename, 'rb')
            encrypted = file_r.read()

            decrypted = self.__cipher__.decrypt(encrypted)

            file_w = open(_decryptedFilename, 'wb')
            file_w.write(decrypted)
        except cryptography.exceptions as c:
            return 'Failed'

        file_w.close()
        file_r.close()
        print('Decryption was a success')

    def __saveKey__(self):
        try:
            filekey = open('filekey.txt', 'wb')
            filekey.write(self.__secretKey__)
        except:
            raise Exception('Failed to write to the generated key.')

        filekey.close()
        self.__info__ += "The key has been generated and saved in the 'filekey.key' file."


E1 = Encoding()

#E1.Encrypt('Test1', '12345')

E1.Decrypt('Test1', 'newTest1')
