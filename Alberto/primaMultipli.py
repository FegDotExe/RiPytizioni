def primaMultipli(seq,m):
    i=0
    while i<len(seq):
        if seq[i]%m==0:
            j=i
            valoreTemp=seq[i]
            while j>0 and seq[j-1]%m!=0:
                seq[j]=seq[j-1]
                j-=1
            seq[j]=valoreTemp
        i+=1
    return seq

print(primaMultipli([1,6,4,12,3,30],3))