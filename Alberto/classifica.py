def classifica(seq):
    output=[]
    i=0
    while i<len(seq):
        posizione=1
        j=0
        while j<len(seq):
            if i!=j and seq[i]>seq[j]:
                posizione+=1
            j+=1
        output.append(posizione)
        i+=1
    return output

print(classifica([5.14,4.22,6.89,3.08,4.71]))