import random
class crypt:
    def en(): #encrypts a message by rearranging the letters
        message = input('What is the message to encrypt? ') #asks for a message
        backwardslist = list(message[i] for i in range(len(message)-1, -1, -1)) #creates a backwards list of the string
        i = 0
        encryptedmessage = ''
        while i < len(backwardslist): #adds every letter to the encrypted message with a random letter in between
            encryptedmessage = encryptedmessage + backwardslist[i] + random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.;?,&$ ')
            i += 1
        print('The encrypted message is: ', encryptedmessage)

    def de(): #de-encrypts an encrypted message
        encryptedmessage = input('What is the encrypted message? ')
        k = 0
        almostdecrypted = ''
        while k < (len(encryptedmessage)-1): #ignores every random letter and adds the real message to the string
            almostdecrypted = almostdecrypted +encryptedmessage[k]
            k += 2
        backwardslist = list(almostdecrypted[k] for k in range(len(almostdecrypted)-1, -1, -1)) #creates a backwards list of the string
        j = 0
        decryptedmessage = ''
        while j < len(backwardslist):
            decryptedmessage = decryptedmessage + backwardslist[j]
            j += 1
        print('The decrypted message is: ', decryptedmessage)

crypt.en()
crypt.de()
