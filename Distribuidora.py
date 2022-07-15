#Exercício 3
import json

with open('dados.json') as file:
    data = json.load(file)

valoresDiarios = [element['valor'] for element in data]
valoresDiariosSemZero = [x for x in valoresDiarios if x != 0.0]

menorFatu = min(valoresDiariosSemZero)
print(f"Menor faturamento mensal foi: {menorFatu}")
maiorFatu = max(valoresDiariosSemZero)
print(f"Maior faturamento mensal foi: {maiorFatu}")

médiaMensal = sum(valoresDiariosSemZero)/len(valoresDiariosSemZero)
print(f"Média mensal foi de: {médiaMensal}")

count = 0

for x in valoresDiarios:
    if x > médiaMensal:
        count += 1

fatuMaiorMean = count

print(f"Número de dias no mês que o valor do faturamento diário foi superior à média mensal é de: {fatuMaiorMean}")