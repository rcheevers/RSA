import json

def encrypt(m,name="Master"):
    
    file = open("RSAKeys.json","r")
    keyDict = json.load(file)
    publicD = keyDict[name]["d"]
    publicN = keyDict[name]["n"]
    file.close()
    return pow(m,publicD,publicN) 

def decrypt(c,name="Master"):
    file = open("RSAKeys.json","r")
    keyDict = json.load(file)
    publicE = keyDict[name]["e"]
    publicN = keyDict[name]["n"]
    file.close()
    return pow(c,publicE,publicN) 
