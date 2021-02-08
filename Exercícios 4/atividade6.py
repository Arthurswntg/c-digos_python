ano = 2021

while True:
    nasc = int(input("Informe seu ano de nascimento: "))

    idade = ano - nasc

    if(idade < 18):
        print("Idade insuficiente\n")
    
    else:
        print("{} anos, idade suficiente\n".format(idade))
    
        break

print("Cadastro feito")