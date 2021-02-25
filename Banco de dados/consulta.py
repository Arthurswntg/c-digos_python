import pymysql

# Estabelecer a conexão

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'turma_sistema'
)

consulta = conexao.cursor()# a função cursor é importante pois permite a interação com o banco de dados

sql = "select * from disciplina where carga_horaria >= 150"

consulta.execute(sql)

# exibir a consulta personalizada

resultado = consulta.fetchall()

for itens in resultado:
    print(f"O nome da disciplina é {itens[2]} e tem a carga horária de {itens[3]} horas")


conexao.close() # Encerrando a conexão

