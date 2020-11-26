import json

def encrypt(m,name="Master"):
    
    file = open("RSAKeys.json","r") #assumes RSAKeys.json exists and has a value of name, else throws an error
    keyDict = json.load(file)
    publicD = keyDict[name]["d"]
    publicN = keyDict[name]["n"]
    file.close()
    return pow(m,publicD,publicN) #returns c, the ciphertext

def decrypt(c,name="Master"):
    file = open("RSAKeys.json","r") #assumes RSAKeys.json exists and has a value of name, else throws an error
    keyDict = json.load(file)
    publicE = keyDict[name]["e"]
    publicN = keyDict[name]["n"]
    file.close()
    return pow(c,publicE,publicN) #returns m, the message

#To-Do:
#add more comments
#write my own pow function
#add sign and verify signiture functions
#use more cryptographically secure random number generator
#add padding scheme
#add method to convert messages into numbers automatically
#protect against some common attacks against badly implimented RSA
    #Fermat factorization and Wiener's Attack
    #padding should protect against Coppersmith's Attack
    #see if i can find any others
#implement the rest of the signal protocol
    #Diffie-Hellman
    #Eliptical curve
    #Advanced Encryption Standard
    #Secure Hash Algorithm
