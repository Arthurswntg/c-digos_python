pessoas = {
    "nome":"Arthur",
    "idade":21,
    "Bairro":"Bequimão"
    }

print(pessoas)

print("Olá {}, você tem {} anos e mora no bairro {}\n\n".format(pessoas['nome'],pessoas['idade'],pessoas['Bairro']))

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for chave, valor in pessoas.items():
    print(f"{chave.title()} = {valor}")


print(f"O tamanho do dicionário é {len(pessoas)}")

pessoas.update({'sexo':'m'})
print(pessoas)


print("\n\n")

lista = []
for cont in range(0,2):
    pessoas["nome"] = input("Informe seu nome: ")
    pessoas["idade"] = int(input("Informe sua idade: "))
    pessoas["Bairro"] = input("Informe seu bairro: ")
    pessoas["sexo"] = input("Informe seu sexo: ")

    lista.append(pessoas.copy())


print(lista)

print(lista[0]['nome'])



