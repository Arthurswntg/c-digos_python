from os import system

soma = 0 

for i in range(1, 11):
    idade = int(input("Informe a idade da {}° pessoa: ".format(i)))

    soma = soma + idade

    system("cls")

media = soma/i

if media <= 25:
    print("A turma é jovem")

elif media > 25 and media <= 60:
    print("A turma é adulta")

else:
    print("A turma é idosa")


print("\n\n")
