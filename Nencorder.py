import sys, os, random, time, os
from pathlib import Path
from textwrap import wrap
random.seed(version=int(time.time()))

class Generator(object):
    def __init__(self):
        super().__init__()
        self.letters = ["1", "2", "3", '4', '5', '6', '7', '8', '9', '0',
         "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]",
         "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "|", "z",
         "x", "c", "v", "b", "n", "m", ",", ".", "/", "Q", "W", "E",
         "R", "T", "Y", "U", "I", "O", "P", "{", "}", "A", "S", "D",
         "F", "G", "H", "J", "K", "L", ":", "Z", "X", "C", "V", "B",
         "N", "M", ",", "?", "!", "@", "#", "$", "%", "^", "&", "*",
         "(", ")", "_", "-", "=", "+", "'", "й", "ц", "у", "к", "е",
         "н", "г", "ш", "щ", "з", "х", "ъ", "ф", "ы", "в", "а", "п",
         "р", "о", "л", "д", "ж", "э", "я", "ч", "с", "м", "и", "т",
         "ь", "б", "ю", "Й", "Ц", "У", "К", "Е", "Н", "Г", "Ш", "Щ",
         "З", "Х", "Ъ", "Ф", "Ы", "В", "А", "П", "Р", "О", "Л", "Д",
         "Ж", "Э", "Я", "Ч", "С", "М", "И", "Т", "Ь", "Б", "Ю"]
        self.keys = {}
    
    def generateKeys(self):
        for letter in self.letters:
            self.keys[letter] = ''.join(str(random.randint(0, 9)) for i in range(10))
        print('[!] Nencoder -> keys generated!')

    def crypt(self, text: str):
        cryptedtext = ''
        for line in text.split('\n'):
            for word in line.split(" "):
                for letter in list(word):
                    cryptedtext += self.keys[letter]
        print(f'[!] Nencoder -> {cryptedtext}')
    
    def encrypt(self, cryptedtext: str):
        try:   
            encryptedtext = ''
            for letter in wrap(cryptedtext, 10):
                encryptedtext += get_key(letter, self.keys)
            print(f'[!] Nencoder -> {encryptedtext}')
        except TypeError:
            print(f'[!] Nencoder -> Wrong text')
            
    def openKeys(self, path: str):
        try: 
            if os.path.isfile(path):
                with open(path, 'r') as filekeys:
                    i = 0
                    for value in wrap(filekeys.read(), 10):
                        self.keys[self.letters[i]] = value
                        i += 1
                print('[!] Nencoder -> keys readed!')
            else:
                print('[!] Nencoder -> File not exist!')
        except:
            print("[!] Nencoder -> FATAL ERROR")

    def saveKeys(self, path):
        try:
            with open(path, 'w') as filekeys:
                keys = ''
                for key, value in self.keys.items():
                    keys += f'{value}'
                filekeys.writelines(keys)
                filekeys.close()
            print('[!] Nencoder -> keys saved!')
        except PermissionError as error:
            print(f'[!] Nencoder -> {error}')
        except FileNotFoundError as error:
            print(f'[!] Nencoder -> {error}')
        except:
            print(f'[!] Nencoder -> FATAL ERROR')

    def readKeys(self):
        keys = ''
        i = 0
        for key, value in self.keys.items():
            if i == 0:
                keys += f'{key} -> {value}'
            elif i < 5 and i != 0:
                keys += f'          {key} -> {value}'
            elif i == 5:
                i = 0
                keys += '\n' 
                continue
            i += 1
        print(keys)

def get_space(word, max):
    return ' ' * (max - len(list(word)))

def get_key(val, keys):
    for key, value in keys.items():
        if val == value:
            return key

def Help():
    commands = [['help', 'Get help menu'], ['crypt', 'Crypt text'], ['encrypt', 'Encrypt text'], ['read', 'Read keys'],
        ['open', 'Open keys'], ['save', 'Save keys'], ['generate', 'Generate keys'], ['exit', 'Close program']]
    for command in commands:
        print(f'{commands.index(command) + 1} -> {command[0]}{get_space(command[0], 8)}: {command[1]}')

def menu(crypter: Generator):
    Help()
    while True:
        inputOk = input(f'Nencoder: menu -> ')
        if inputOk == 'help' or inputOk == '1': Help()
        elif inputOk == 'crypt' or inputOk == '2': 
            text = input('Nencoder: crypter -> ')
            crypter.crypt(text)
        elif inputOk == 'encrypt' or inputOk == '3':
            text = input('Nencoder: encrypter -> ')
            crypter.encrypt(text)
        elif inputOk == 'read' or inputOk == '4':
            crypter.readKeys()
        elif inputOk == 'open' or inputOk == '5':
            path = input('Nencoder: open -> ')
            crypter.openKeys(path)
        elif inputOk == 'save' or inputOk == '6': 
            path = input('Nencoder: save -> ')
            crypter.saveKeys(path)
        elif inputOk == 'generate' or inputOk == '7':  
            crypter.generateKeys()
        elif inputOk == 'exit' or inputOk == '8':   
            exit(0)
        else:
            continue

def main():
    crypter = Generator()
    menu(crypter)


try:
    main()
except KeyboardInterrupt:
    exit(f'\n[!] Nencoder -> User closed program!')
