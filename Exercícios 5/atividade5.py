from random import randint

aleatorio = []
    aleatorio.append(randint(1,900))

for cont in range(3,0,-1):
    print(f"Voce tem {cont} chances para descobrir um dos valores da lista")

    op = int(input("Informe um valor qualquer: "))

    if op in aleatorio:
        print(f"{'PARABÉNS':*^40}")
        print("Você encontrou")

        break
    else:
        print("Tente novamente: ")
    
