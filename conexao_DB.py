import mysql.connector
from uteis import log


def conexao_db():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="*********",
            database="clientes")
        log('Conexão realizada com sucesso!')
        return conexao
    except mysql.connector.Error as erro:
        log(erro)
