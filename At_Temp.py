import time

from Utilitarios import Temperatura
from bd import BancoDados
from Nitrogenio import Nitrogenio

if BancoDados().consulta_init() == []:
    status = "ANALISANDO"
    temp_ant = Temperatura.temp()
    BancoDados().incluir("Dublin", temp_ant, status)
    time.sleep(10)
    temp = Temperatura.temp()
    status = Nitrogenio().VerificaStatus(temp, temp_ant)
    BancoDados().incluir("Dublin", temp, status)
else:
    temp = Temperatura.temp()
    temps_ant = BancoDados().consulta()
    temp_ant=temps_ant[0][0]
    status = Nitrogenio().VerificaStatus(temp, temp_ant)
    BancoDados().incluir("Dublin", temp, status)