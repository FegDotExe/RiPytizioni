def zeriInTesta(seq):
    zeri=[]
    non_zeri=[]
    for elemento in seq:
        if elemento==0:
            zeri.append(elemento)
        else:
            non_zeri.append(elemento)
    return zeri+non_zeri

print(zeriInTesta([1,6,0,5,0,2,0]))