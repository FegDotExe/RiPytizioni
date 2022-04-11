def zeriInTesta(seq):
    i=0
    while i<len(seq):
        if seq[i]==0:
            j=i
            while j>0 and seq[j-1]!=0:
                seq[j]=seq[j-1]
                j-=1
            seq[j]=0
        i+=1
    return seq

print(zeriInTesta([1,6,0,5,0,2,0]))