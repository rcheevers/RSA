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
    return pow(signature,E,N)==hashM #returns if signature is valid or not

def signatureVerify(signiture, ciphertext, public, private):
    keys = open("RSAKeys.json","r") 
    keyDict = json.load(keys)
    publicE = keyDict[public]["e"]
    publicN = keyDict[public]["n"]
    privateD = keyDict[private]["d"]
    privateN = keyDict[private]["n"]
    keys.close()
    hashM = int(hashlib.sha512(str(pow(cyphertext,privateD,privateN)).encode()).hexdigest(),16)
    return pow(signature,publicE,publicN)==hashM #returns if signature is valid or not
