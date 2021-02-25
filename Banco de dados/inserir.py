import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'turma_sistema'
)

cod = int(input("Informe o código da disciplina: "))
nome = str(input("Informe o nome da disciplina: ")).lower()
descricao = str(input("Informe a descrição da disciplina: ")).lower()
ch = int(input("Informe a carga horária da disciplina: "))

comando = "insert into disciplina values(%s,%s,%s,%s)"

valores = (cod,descricao,nome,ch)

consulta = conexao.cursor()

consulta.execute(comando,valores)

conexao.commit() # gravar os dados no banco

print(consulta.rowcount,"linha(s) inserida com sucesso!")
conexao.close()