def sommaDispariDaA(inizio,fine):
    numero_valori_sommati=0
    i=0
    somma=0

    while (inizio+i)<fine:
        if (inizio+i)%2!=0:
            somma=somma+(inizio+i)
            numero_valori_sommati+=1
        
        i=i+1
    
    return somma, numero_valori_sommati


somma, numero_valori = sommaDispariDaA(5,10)

print(somma)
print(numero_valori)