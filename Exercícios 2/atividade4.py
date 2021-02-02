km = float(input("Informe quantos km o carro faz por litro: "))
restante = float(input("Informe quantos litros de gasolina tem no carro atualmente: "))
dist = float(input("Informe quantos km deseja percorrer: "))


if ((dist/km) < restante):
    print("Pode ir tranquilo que dá pra chegar no destino")

else:
    print("Você vai precisar abastecer {:.2f} litros \n\n".format(dist/km-restante))

