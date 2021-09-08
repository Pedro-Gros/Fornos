import mariadb
import sys
from Conexao import ConexaoDB

class BancoDados():
    def incluir(self, maquina, data, temp):
        c = ConexaoDB()
        sql = f"INSERT INTO temp VALUES ('{maquina}','{data}','{temp}')"
        c.execute_DML(sql)

    def consulta(self):
        c = ConexaoDB()
        sql = f"SELECT * FROM temp "
        res = c.executa_DQL(sql)
        return res

