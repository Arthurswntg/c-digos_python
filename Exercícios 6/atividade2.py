alunos = {}
turma = []


for cont in range(0,3):
    alunos['nome'] = str(input("Informe o nome do aluno {}: ".format(cont+1))).title()
    alunos['nota1'] = float(input(f"Informe a nota 1 de {alunos['nome']}: "))
    alunos['nota2'] = float(input(f"Informe a nota 2 de {alunos['nome']}: "))
    alunos['nota3'] = float(input(f"Informe a nota 3 de {alunos['nome']}: "))
    alunos['media'] = (alunos['nota1'] + alunos['nota2'] + alunos['nota3'])/3

    turma.append(alunos.copy())
    alunos.clear() #Limpando o dicionário

print("\n", turma, "\n")

for itens in turma:
    for chave, valor in itens.items():
        if chave == "nome":
            print(f"Aluno(a) {valor}",end="")
        if chave == "media":
            print(f" teve média = {valor:.2f}")

print("\n\n")