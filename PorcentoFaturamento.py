#Exercício 4

SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53

totalDist = SP + RJ + MG + ES + OUTROS

porcentSP = SP * 100 / totalDist
print(f"Estado de SP compõe {porcentSP:.2f}% do total mensal da Distribuidora")

porcentRJ = RJ * 100 / totalDist
print(f"Estado de RJ compõe {porcentRJ:.2f}% do total mensal da Distribuidora")

porcentMG = MG * 100 / totalDist
print(f"Estado de MG compõe {porcentMG:.2f}% do total mensal da Distribuidora")

porcentES = ES * 100 / totalDist
print(f"Estado de ES compõe {porcentES:.2f}% do total mensal da Distribuidora")

porcentOUTROS = OUTROS * 100 / totalDist
print(f"Outros Estados compõem {porcentOUTROS:.2f}% do total mensal da Distribuidora")