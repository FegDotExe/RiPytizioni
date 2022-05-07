def intersezione(seq1,seq2):
    intersezione = []
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                intersezione.append(seq1[i])
    return intersezione

print(intersezione([1,7,2,8],[8,3,6,7]))