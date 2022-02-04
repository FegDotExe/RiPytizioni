def scambiaUltimoConPrimo(s):
    if len(s) > 1:
        output=s[-1] + s[1:-1] + s[0]
        return output
    return s