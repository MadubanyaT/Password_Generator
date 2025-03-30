import os.path
import sys

import cryptography
from cryptography.exceptions import InvalidSignature
from cryptography.fernet import Fernet, InvalidToken


class Cryptography:

    def __init__(self, Key=None):
        self.__secretKey = Key or Fernet.generate_key()
        self.__cipher = Fernet(self.__secretKey)
        self.info = ""

    def saveThenEncrypt(self, _password, _webName="", _userName=""):
        self.__saveKey()
        _filename = "Decrypted"

        try:
            if _webName == "":
                _webName = 'Unknown Website'
            if _userName == "":
                _userName = "Unknown Username"

            text = ('Website name: ' + _webName + ', Username: '
                    + _userName + ', Password: ' + _password + '\n').encode('utf-8')

            # Write and Read from the Decrypted file
            if os.path.isfile(_filename):
                file_w = open(_filename, 'ab')
                file_w.write(text)
                file_w.close()

                file_r = open(_filename, 'rb')
                text += file_r.readline()
                file_r.close()
                self.info += '\nThe Decrypted file is appended with new info.'

            # encrypt the text read from the Decrypt file
            encrypted = self.__cipher.encrypt(text)

            if os.path.isfile('Encrypted'):
                self.info += '\nThe Encrypted file was overwritten.'

            # write to the encrypted text to the Encrypted file
            _filename = 'Encrypted'
            file_wE = open(_filename, 'wb')
            file_wE.write(encrypted)
            file_wE.close()
        except Exception as e:
            print(f'Error: {e}')

        self.info += (f'\nYour data was successfully saved and encrypted! Check the {_filename} file.'
                      f'\nYou can delete the decrypted file')
        return self.info

    def Decrypt(self, _encryptedFilename, Key=None):
        _decryptedFilename = 'Decrypted'
        b = False
        if os.path.isfile(_encryptedFilename):
            try:
                key = Fernet(Key)

                file_r = open(_encryptedFilename, 'rb')
                encrypted = file_r.read()

                decrypted = key.decrypt(encrypted)

                file_w = open(_decryptedFilename, 'ab')
                file_w.write(decrypted)

                file_w.close()
                file_r.close()
                b = True
            except InvalidToken as i:
                print(f'Key Error: {i}')
            except Exception as e:
                print(f'Decryption Error: {e}')

            if b:
                self.info = f'Decryption was a success! Check the {_decryptedFilename} file.'
        else:
            self.info = '''The file doesn't exists.'''

        return self.info

    def __saveKey(self):
        try:
            filekey = open('KEY', 'wb')
            filekey.write(self.__secretKey)
        except Exception:
            raise Exception('Failed to write to the generated key.')

        filekey.close()
        self.info = "The key has been generated and saved in the 'KEY' file. Keep it safe!"
