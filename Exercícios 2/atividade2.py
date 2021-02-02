peso = float(input("Informe o peso da pessoa em kg: "))
altura = float(input("Informe a altura da pessoa em metros: "))

IMC = (peso/altura**2)

if(IMC < 16):
    print("O IMC é igual a {:.2f} aponta magreza grave".format(IMC))

elif(16 <= IMC < 17):
    print("O IMC é igual a {:.2f} aponta magreza moderada".format(IMC))
    
elif(17 <= IMC < 18.5):
    print("O IMC é igual a {:.2f} aponta magreza leve".format(IMC))
    
elif(18.5 <= IMC < 25):
    print("O IMC é igual a {:.2f} aponta saudável".format(IMC))
    
elif(25 <= IMC < 30):
    print("O IMC é igual a {:.2f} aponta sobrepeso".format(IMC))
    
elif(30 <= IMC < 35):
    print("O IMC é igual a {:.2f} aponta obesidade grau I".format(IMC))
    
elif(35 <= IMC < 40):
    print("O IMC é igual a {:.2f} aponta obesidade grau II".format(IMC))
    
else:
    print("O IMC é igual a {:.2f} aponta obesidade grau III".format(IMC))
