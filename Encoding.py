import cryptography
from cryptography.exceptions import InvalidSignature
from cryptography.fernet import Fernet


# Giving a user a default file instead of their input e.g Encrypted, Decrypted


class Cryptography:

    def __init__(self, Key=None):
        self.__secretKey = Key or Fernet.generate_key()
        self.__cipher = Fernet(self.__secretKey)
        self.info = ""

    def saveThenEncrypt(self,  _password, _webName="", _userName=""):
        self.__saveKey()
        
        _filename = "Decrypt"

        try:
            if _webName == "":
                _webName = 'Unknown Website'
            if _userName == "":
                _userName = "Unknown Username"

            text = ('Website name: ' + _webName + ', Username: '
                    + _userName + ', Password: ' + _password + '\n').encode('utf-8')

            if _filename == 'Decrypted':
                file_w = open(_filename, 'ab')
                file_w.write(text)
                file_w.close()

                file_r = open(_filename, 'rb')
                text += file_r.readline()
                file_r.close()

            encrypted = self.__cipher.encrypt(text)

            _filename = 'Encrypted'
            file_wE = open(_filename, 'ab')
            file_wE.write(encrypted)
        except:
            raise Exception('An error occurred.')

        file_wE.close()
        self.info += (f'\nYour data was successfully saved and encrypted! Check the {_filename} file.'
                      f'\nYou can delete the decrypted file')
        return self.info

    def Decrypt(self, _encryptedFilename, Key=None, _decryptedFilename=''):
        key = Fernet(Key)

        try:
            file_r = open(_encryptedFilename, 'rb')
            encrypted = file_r.read()

            decrypted = key.decrypt(encrypted)

            if _decryptedFilename == '':
                _decryptedFilename = 'Decrypt_default.txt'

            _decryptedFilename = _decryptedFilename.replace('E_','')
            if _decryptedFilename.rfind('D_') == -1:
                _decryptedFilename = 'D_' + _decryptedFilename

            file_w = open(_decryptedFilename, 'ab')
            file_w.write(decrypted)
        except cryptography.exceptions as c:
            return 'Failed'

        file_w.close()
        file_r.close()
        self.info = f'Decryption was a success! Check the {_decryptedFilename} file.'

        return self.info

    def __saveKey(self):
        try:
            filekey = open('KEY', 'wb')
            filekey.write(self.__secretKey)
        except:
            raise Exception('Failed to write to the generated key.')

        filekey.close()
        self.info = "The key has been generated and saved in the 'KEY' file. Keep it safe!"
