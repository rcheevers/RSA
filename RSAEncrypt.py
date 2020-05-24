
def encrypt(m):
    
    file = open("RSAKeys.txt","r")
    file.readline()
    public = file.readline()
    file.close()
    i = 0
    while i < len(public):
        if "," == public[i]:
            commaIndex = i
            break
        i = i + 1
    e = public[12:commaIndex]
    n = public[commaIndex+2:-1]
    return pow(m,e,n)
    
