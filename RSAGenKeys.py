import secrets
import json
import os
import random

def createKeys(name="Master"):
    p = secrets.randbits(2048)
    q = secrets.randbits(2048)
    while (not isPrime(p)):
        p = secrets.randbits(2048)
    while (not isPrime(q)):
        q = secrets.randbits(2048)
    n = p*q
    PhiN = (p-1)*(q-1)//GCD(p-1,q-1)
    e = setE(PhiN)
    d = EEA(e,PhiN)

    newKey = { #add key to json file
        "d" : d,
        "n" : n,
        "e" : e
    }

    if(os.path.isfile("RSAKeys.json") and os.access("RSAKeys.json", os.R_OK)):
        with open("RSAKeys.json","w") as file:
            keyDict = json.load(file)
            keyDict[name] = newKey
            json.dump(keyDict, file)
    else:
        with open("RSAKeys.json","w") as file:
            keyDict = {}
            keyDict[name] = newKey
            json.dump(keyDict, file)
    
def isPrime(n): #fermats compositeness test
    k = 128
    while (k>0):
        a = random.randint(2,n-2) 
        if (pow(a,n-1,n) != 1):   
            return False
        k = k-1
    return True

    
def setE(PhiN):
    if(goodE(65537,PhiN)):
        return 65537
    e = 2
    while(not goodE(e,PhiN)):
        e = e + 1
    return e


def goodE(e,PhiN):
    return (e>1 and e<PhiN and GCD(e,PhiN)==1)

def GCD(a,b): #Greatest Common Divisor
    while(b>0):
        temp = a % b
        a = b
        b = temp
    return a

def EEA(a,b): #Extended Euclidean Algorithm
    r0 = a
    r1 = b
    t0 = 0
    t1 = 1
    s0 = 1
    s1 = 0
    while(r1 > 0):
        q = r0 // r1
        rTemp = r0 - q * r1
        tTemp = t0 - q * t1
        sTemp = s0 - q * s1
        t0 = t1
        s0 = s1
        r0 = r1
        t1 = tTemp
        s1 = sTemp
        r1 = rTemp
    if (s0 < 0):
        s0 = s0 + b
    return s0

