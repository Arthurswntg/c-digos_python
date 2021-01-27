m_quad = 850.0
base = float(input("Digite a largura do terreno em metros: "))
altura = float(input("Digite o comprimento do terreno em metros: "))
area = (base*altura)

custo_total = (area*m_quad)

print("\nO custo total para uma área de {} m é igual a R$ {}".format(area, custo_total))
