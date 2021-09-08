import mariadb
import sys

class ConexaoDB:
    def __init__(self, host = 'localhost',
                       user ='root',
                       pwd  ='engenhariatdb',
                       db = 'TEMP'):
        self.host = host
        self.user = user
        self.pwd  = pwd
        self.db = db


    def conecta(self):
        self.con = mariadb.connect(host=self.host,
                                   user=self.user,
                                   password=self.pwd,
                                   database = self.db
                                   )
        self.cur = self.con.cursor()

    def desconecta(self):
        self.con.close()

    def executa_DQL(self, sql):
        self.conecta()
        self.cur.execute(sql)
        res = self.cur.fetchall()
        self.desconecta()
        return res

    def execute_DML(self,sql):
        self.conecta()
        self.cur.execute(sql)
        self.con.commit()
        self.desconecta()