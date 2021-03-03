# Superclasse
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

        self.nomeClasse = self.__class__.__name__ #pega o nome da classe
    

    def mostraClasse(self):
        print(f"{self.nomeClasse} = seu nome é {self.nome}")

# Subclasse
class Aluno(Pessoa):
    def __init__(self,nome,idade,matricula):
        Pessoa.__init__(self,nome,idade)
        self.matricula = matricula

    def mostraAluno(self):
        print(f"{self.nomeClasse} = sou aluno e meu nome é {self.nome}")

class Professor(Pessoa):
    def __init__(self,nome,idade,salario):
        Pessoa.__init__(self,nome,idade)
        self.salario = salario

    def mostraProfessor(self):
        print(f"{self.nomeClasse} = sou professor e meu nome é {self.nome}")
        
