import itertools, os, json

SUFFIX = -4

class CaesarCipher:
    # Consts
    NUM_LETTERS = 26
    
    def __init__(self, key):
        """ Creator of CaesarCipher object"""
        self.key = key
    
    def encrypt(self, message):
        """ Encrypting given message by self key """ 
        try:
            encryptedMessage = ""
            # Encrypt each letter in the word
            for letter in message:
                # Keep every Non-letter in the sentence
                if letter.isalpha():
                    encryptedMessage += self.encryptLetter(letter, self.key)
                else:
                    encryptedMessage += letter
            
            return encryptedMessage
        except:
            return

    def decrypt(self, encryptedMessage):
        """ Decrypting given message by self key """ 
        try:
            originalMessage = ""
            # Decrypt each letter in the word (call encryptLettter with negative value of shifting)
            for letter in encryptedMessage:
                # Keep every Non-letter in the sentence
                if letter.isalpha():
                    originalMessage += self.encryptLetter(letter, -self.key)
                else:
                    originalMessage += letter
                     
            return originalMessage
        except:
            return
    
    def encryptLetter(self, letter, shift):
        """ Encrypting given letter by given shift """ 
        
        # Values validation check
        if ((not isinstance(shift, int)) or (len(letter) != 1) or (not(letter.isalpha()))):
            raise ValueError
        
        # Encrypt letter - Lower letter case
        if letter.islower():
            return chr(ord('a') + ((ord(letter) - ord('a') + shift) % self.NUM_LETTERS))
        
        # Encrypt letter - Upper letter case
        if letter.isupper():
            return chr(ord('A') + ((ord(letter) - ord('A') + shift) % self.NUM_LETTERS))

class VigenereCipher:
    # Consts
    NUM_LETTERS = 26
    
    def __init__(self, keyList):
        """ Creator of VigenereCipher object"""
        self.keyList = keyList
    
    def encrypt(self, message):
        """ Encrypting given message by self keyList """ 
        try:
            currentKey = itertools.cycle(self.keyList)
            encryptedMessage = ""
            # Encrypt each letter in the word
            for letter in message:
                # Keep every Non-letter in the sentence
                if letter.isalpha():
                    encryptedMessage += self.encryptLetter(letter, next(currentKey))
                else:
                    encryptedMessage += letter
            
            return encryptedMessage
        except:
            return

    def decrypt(self, encryptedMessage):
        """ Decrypting given message by self keyList """ 
        try:
            currentKey = itertools.cycle(self.keyList)
            originalMessage = ""
            # Decrypt each letter in the word (call encryptLettter with negative value of shifting)
            for letter in encryptedMessage:
                # Keep every Non-letter in the sentence
                if letter.isalpha():
                    originalMessage += self.encryptLetter(letter, -next(currentKey))
                else:
                    originalMessage += letter
                     
            return originalMessage
        except:
            return
    
    def encryptLetter(self, letter, shift):
        """ Encrypting given letter by given shift """ 
        
        # Values validation check
        if ((not isinstance(shift, int)) or (len(letter) != 1) or (not(letter.isalpha()))):
            raise ValueError
        
        # Encrypt letter - Lower letter case
        if letter.islower():
            return chr(ord('a') + ((ord(letter) - ord('a') + shift) % self.NUM_LETTERS))
        
        # Encrypt letter - Upper letter case
        if letter.isupper():
            return chr(ord('A') + ((ord(letter) - ord('A') + shift) % self.NUM_LETTERS))
        
def getVigenereFromStr(string):
    """ Creating and returnong new VigenereCipher object with ketList which created by given string int values"""
    keyList = []
    for letter in string:
        if letter.isalpha() and letter.islower():
            keyList.append(ord(letter) - ord("a"))
        if letter.isalpha() and letter.isupper():
            keyList.append(ord(letter) - ord("A"))
    return VigenereCipher(keyList)

def loadEncryptionSystem(dirPath):
    """ Load the encrypting system and changes the file in the given path acording to the config file. """
    # Extract configuration values
    try:
        encryptionType, encrypt, key = loadConfigoration(dirPath)
    
        # Process files in the directory
        for fileName in os.listdir(dirPath):
            filePath = os.path.join(dirPath, fileName)
            if os.path.isfile(filePath):
                if encrypt:
                    encryptFile(fileName, filePath, encryptionType, key)
                else:
                    decryptFile(fileName, filePath, encryptionType, key)
    except:
        return 
                        
def loadConfigoration(dirPath):
    """ Load the configuration file and returning the configuration values """
    configPath = os.path.join(dirPath, 'config.json')
    with open(configPath, 'r') as configFile:
        config = json.load(configFile)
        
    return config['type'], config['encrypt'], config['key']

def encryptFile(fileName, filePath, encryptionType, key):
    """ Encrypting given file and and write it to new .enc file. """
    # Make sure it will encrypt only txt files
    if fileName.endswith(".txt"):
        cipher = getCipher(encryptionType, key)
        
        # Encrypt acording to the config encryptionType and write it to new .enc file
        encryptedText = cipher.encrypt(readFile(filePath))
        encryptedFilePath = filePath[:SUFFIX] + ".enc"
        writeFile(encryptedFilePath, encryptedText)
 
def decryptFile(fileName, filePath, encryptionType, key):
    """ Decrypting given file and and write it to new .txt file. """
    # Make sure it will encrypt only enc files
    if fileName.endswith(".enc"):
        cipher = getCipher(encryptionType, key)
        
        # Decrypt acording to the config encryptionType and write it to new .txt file
        encryptedText = cipher.decrypt(readFile(filePath))
        encryptedFilePath = filePath[:SUFFIX] + ".txt"
        writeFile(encryptedFilePath, encryptedText)

def getCipher(encryptionType, key):
    """ Gets an encryptionType and a key and returns a proper cipher object """
    if encryptionType == "Vigenere":
        return getVigenereFromStr(key)
           
    if encryptionType == "Caeser":
        return CaesarCipher(key)
    
    raise ValueError
            
def readFile(filePath):
    # Read the contents of a file
    with open(filePath, "r") as openFile:
        return openFile.read()

def writeFile(filePath, content):
    # Write content to a file
    with open(filePath, "w") as openFile:
        openFile.write(content)