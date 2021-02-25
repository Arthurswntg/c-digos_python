valores = list()
pares = []

for cont in range(0,10):
    valores.append(int(input(f"informe o valor{cont+1}: ")))

    if valores[cont] % 2 == 0:
        pares.append(valores[cont])

for cont in range(0,len(pares)):
    if pares[cont] in valores:
        valores.remove(pares[cont])

del(pares)

print(f"Lista sem os valores pares: {valores}\n\n")