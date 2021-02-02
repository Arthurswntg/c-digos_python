velPerm = float(input("Qual a velocidade permitida? "))
velMotorista = float(input("Qual a velocidade do motorista? "))

velPerm20 = (velPerm*0.2) + velPerm

velPerm50 = (velPerm*0.5) + velPerm

if (velMotorista <= velPerm):
    print("Tudo certo, não precisa pagar multa")

elif (velMotorista > velPerm and velMotorista <= velPerm20):
    print("Você cometeu infração média\nAssim irá pagar R$ 85.00 e receber 4 pontos na carteira")

elif (velMotorista > velPerm20 and velMotorista <= velPerm50):
    print("Você cometeu infração grave\nAssim irá pagar R$ 127.00 e receber 5 pontos na carteira")

elif (velMotorista > velPerm50):
    print("Você cometeu infração gravíssima\nAssim irá pagar R$ 574.00\nReceber 7 pontos na carteira\nCarteira apreendida\nDireito de dirigir suspenso")