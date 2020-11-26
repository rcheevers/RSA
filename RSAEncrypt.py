import json
import hashlib

def encrypt(message, public="Master"): 
    keys = open("RSAKeys.json","r") #assumes RSAKeys.json exists and has a value of name, else throws an error
    keyDict = json.load(keys)
    E = keyDict[public]["e"]
    N = keyDict[public]["n"]
    keys.close()
    return pow(message,E,N) #returns the ciphertext

def decrypt(cyphertext, private="Master"):
    file = open("RSAKeys.json","r") 
    keyDict = json.load(file)
    E = keyDict[private]["d"]
    N = keyDict[private]["n"]
    keys.close()
    return pow(cyphertext,E,N) #returns the message

def sign(message, private="Master"): 
    keys = open("RSAKeys.json","r") 
    keyDict = json.load(keys)
    E = keyDict[private]["d"]
    N = keyDict[private]["n"]
    keys.close()
    hashM = int(hashlib.sha512(str(message).encode()).hexdigest(),16)
    return pow(hashM,E,N) #returns signature

def signatureVerify(signiture, message, public="Master"):
    keys = open("RSAKeys.json","r") 
    keyDict = json.load(keys)
    E = keyDict[public]["e"]
    N = keyDict[public]["n"]
    keys.close()
    hashM = int(hashlib.sha512(str(message).encode()).hexdigest(),16)
    return pow(signiture,E,N)==hashM #returns if signature is valid or not

def signatureVerify(signiture, ciphertext, public, private):
    keys = open("RSAKeys.json","r") 
    keyDict = json.load(keys)
    publicE = keyDict[public]["e"]
    publicN = keyDict[public]["n"]
    privateD = keyDict[private]["d"]
    privateN = keyDict[private]["n"]
    keys.close()
    hashM = int(hashlib.sha512(str(pow(cyphertext,privateD,privateN)).encode()).hexdigest(),16)
    return pow(signiture,publicE,publicN)==hashM #returns if signature is valid or not

#To-Do:
#write my own pow function
    #chinese remainder theorem
    #square and multiply algorithm
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
