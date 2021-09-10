from Conexao import ConexaoDB

class BancoDados():
    def incluir(self, maquina, temp):
        c = ConexaoDB()
        sql = f"INSERT INTO temp VALUES ('{maquina}', Now(),'{temp}')"
        c.execute_DML(sql)

    def consulta(self):
        c = ConexaoDB()
        sql = f"SELECT temperatura FROM temp ORDER BY data DESC LIMIT 3 "
        res = c.executa_DQL(sql)
        return res

