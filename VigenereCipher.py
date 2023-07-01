
class VigenereCipher:
    NUM_LETTERS = 26
    
    def __init__(self, keyList):
        self.keyList = keyList
    
    def encrypt(self, message):
        try:
            encryptedMessage = ""
            keyIndex = 0
            for letter in message:
                print(letter)
                encryptedMessage += self.encryptLetter(letter, self.keyList[keyIndex])
                keyIndex += 1
                
                # Make sure not crossing list borders
                if keyIndex >= len(self.keyList):
                    keyIndex = 0
            return encryptedMessage
        except:
            print("Invalid message")

    def encryptLetter(self, letter, shift):
        # Values validation check
        if ((shift < 0) or (not isinstance(shift, int)) or (len(letter) != 1) or not(letter.isalpha())):
            raise ValueError
        
        # Encrypt letter - Lower letter case
        if letter.islower:
            return ord('a') + ((ord(letter) - ord('a') + shift) % self.NUM_LETTERS)
        
        # Encrypt letter - Upper letter case
        if letter.isupper:
            return ord('A') + ((ord(letter) - ord('A') + shift) % self.NUM_LETTERS)
    
stam = VigenereCipher([1])
print(stam.encrypt("abc"))