def conta(s1, s2):
    cont=0
    for i in range(len(s1)):
        if s1[i]==s2:
            cont+=1
    return cont

def piuFrequente(s):
    max=0
    stringa=""
    for i in range(len(s)):
        cont=conta(s,s[i])
        if cont>max:
            max=cont
            stringa=s[i]
    return stringa, max

print(piuFrequente("calamaro"))