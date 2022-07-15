#Exercício 5

input = input("Digite uma string que será invertida: ")

inputRevertido=[]
i = len(input)
while i > 0: 
    inputRevertido += input[i-1]
    i = i - 1


print("String Revertida:",''.join(inputRevertido)) 