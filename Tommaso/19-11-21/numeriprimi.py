numero=13

i=2
is_prime=True

while i<numero:
    print("Provo a fare "+str(numero)+"/"+str(i))
    if numero%i==0:
        is_prime=False
    i=i+1#Si può scrivere anche i+=1

print(is_prime)

def is_prime(number):
    i=2
    is_prime=True

    while i<number:
        if number%i==0:
            is_prime=False
            break
        i=i+1

    return is_prime

numero=int(input("Scrivi un numero>"))

print(is_prime(numero))