def quanteMaiuscole(stringa):
    cont = 0
    for i in stringa:
        if i.isupper():
            cont += 1
    return cont

print(quanteMaiuscole("Alberto"))