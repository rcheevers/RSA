import random
systemRandom = random.SystemRandom()

def rand():
    return systemRandom.randint(2**127,2**128)

def createKeys():
    p = rand()
    q = rand()
    while (not isPrime(p)):
        p = rand()
    print(p)
    while (not isPrime(q)):
        q = rand()
    print(q)
    n = p*q
    print(n)
    PhiN = (p-1)*(q-1)//GCD(p-1,q-1)
    print(PhiN)
    e = setE(PhiN)
    print(e)
    d = EEA(e,PhiN)
    print(d)
    file = open("RSAKeys.txt","a")
    file.write(("Private Key: "+str(d)+", "+str(n)+"\n"))
    file.write(("Public Key: "+str(e)+", "+str(n)+"\n"))
    file.close()

    
def isPrime(n):  
    k = 3
    while (k>0):
        a = systemRandom.randint(2,n-2)
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


def goodE(n,PhiN):
    return (n>1 and n<PhiN and GCD(n,PhiN)==1)

def GCD(a,b):
    while(b>0):
        temp = a % b
        a = b
        b = temp
    return a

def EEA(a,b):
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

    























