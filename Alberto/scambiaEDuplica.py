def scambiaEDuplica(seq):
    output=[]
    i=0
    while i<len(seq):
        if i+1<len(seq):
            output.append(seq[i+1])
            output.append(seq[i])
        else:
            output.append(seq[i])
            output.append(seq[i])
        i+=2
    return output

print(scambiaEDuplica([4,7,1,8,2]))