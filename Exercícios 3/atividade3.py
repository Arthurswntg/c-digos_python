import time
import os

totPessoas = int(input("Serão dadas boas vindas para quantas pessoas? "))

hom = 0
mul = 0

for i in range(1, totPessoas+1):
    nome = input("Qual o seu nome? ")
    sexo = input("Qual o seu sexo? m/f: ")

    if sexo == "m":
        print("Bem vindo Sr. {}".format(nome))
        hom = hom + 1
    
    else:
        print("Bem vindo Sra. {}".format(nome))
        mul = mul + 1
    
    time.sleep(1)
    os.system("cls")

print("Houve um total de {} homens e {} mulheres".format(hom, mul))