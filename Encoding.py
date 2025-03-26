import cryptography
from cryptography.exceptions import InvalidSignature
from cryptography.fernet import Fernet


# This class should not output anything, but write to files.
# The class can receive name of the website for password (but optional)
# Must have to encrypt, decrypt, createKey methods
# It can update the user if the key is created


class Cryptography:

    def __init__(self, Key=None):
        self.__secretKey = Key or Fernet.generate_key()
        self.__cipher = Fernet(self.__secretKey)
        self.info = ""

    def Encrypt(self,  _password, _webName="", _userName="", _filename=""):
        self.__saveKey()

        try:
            if _webName == "":
                _webName = 'Unknown Website'
            if _userName == "":
                _userName = "Unknown Username"
            if _filename == "":
                _filename = "Encrypt_default.txt"

            text = ('Website name: ' + _webName + ', Username: '
                    + _userName + ', Password: ' + _password + '\n').encode('utf-8')

            encrypted = self.__cipher.encrypt(text)

            print(encrypted)
            file_w = open(_filename, 'wb')
            file_w.write(encrypted)
        except:
            raise Exception('An error occurred.')

        file_w.close()
        return self.info + f'\nYour data was successfully saved and encrypted! Check the {_filename} file.'

    def Decrypt(self, _encryptedFilename, Key=None, _decryptedFilename=''):

        key = Fernet(Key)

        try:
            file_r = open(_encryptedFilename, 'rb')
            encrypted = file_r.read()

            decrypted = key.decrypt(encrypted)

            if _decryptedFilename == '':
                _decryptedFilename = 'Decrypt_default.txt'

            file_w = open(_decryptedFilename, 'wb')
            file_w.write(decrypted)
        except cryptography.exceptions as c:
            return 'Failed'

        file_w.close()
        file_r.close()
        self.info = f'Decryption was a success! Check the {_decryptedFilename} file.'

        return self.info

    def __saveKey(self):
        try:
            filekey = open('filekey.txt', 'wb')
            filekey.write(self.__secretKey)
        except:
            raise Exception('Failed to write to the generated key.')

        filekey.close()
        self.info = "The key has been generated and saved in the 'filekey.txt' file. Keep it safe!"
