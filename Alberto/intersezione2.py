def intersezione(seq1,seq2):
    intersezione = []
    for i in range(len(seq1)):
        if seq1[i] in seq2:
            intersezione.append(seq1[i])
    return intersezione

print(intersezione([1,7,2,8],[8,3,6,7]))