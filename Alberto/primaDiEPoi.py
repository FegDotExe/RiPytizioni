def primaDiEPoi(s, c):
    output=""
    for lettera in s:
        if lettera<c:
            output+=lettera
    for lettera in s:
        if lettera>=c:
            output+=lettera
    return output

def primaDiEPoi(s, c):
    pezzo1="" #Si creano due diverse stringhe, una che contenga i caratteri minori,
    pezzo2="" #l'altra che contenga quelli maggiori o uguali
    for lettera in s:
        if lettera<c:
            pezzo1+=lettera
        else:
            pezzo2+=lettera
    return pezzo1+pezzo2 #Si restituisce una composizione dei due pezzi

print(primaDiEPoi("qweartyc","e"))

