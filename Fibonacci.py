#Exercício 2
n = int(input("Informe um número:"))

ultimo=1
penultimo=1
until = 0 + n
if n == 0 or n == 1 or n == 2:
    print("Numero pertence a sequência")
elif n == 4:
    print("Numero não pertence a sequência")
else:
    for count in range(2,until):
        fibo = ultimo + penultimo
        penultimo = ultimo
        ultimo = fibo
        count += 1
        if n == fibo:
            print("Numero pertence a sequência")
            break
        elif fibo > n:
            print("Numero não pertence a sequência")
            break