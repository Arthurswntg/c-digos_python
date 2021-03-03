from heranca2 import Aluno, Professor

a1 = Aluno("Matilda", 23,987)

a1.mostraAluno()

print(f"\nA matricula de {a1.nome} é {a1.matricula}\n")

prof = Professor("Geraldo",54,3250.56)

prof.mostraProfessor()
print(f"\nO Salário de {prof.nome} é R$ {prof.salario}")