import time
from Utilitarios import Temperatura

from bd import BancoDados

while True:
    temp = Temperatura.temp()
    print(temp)
    temps_ant = BancoDados().consulta()
    temp_ant=temps_ant[0][0]
    temp_ant2 = temps_ant[1][0]
    temp_ant3 = temps_ant[2][0]
    print(temp_ant)
    print(temp_ant2)
    print(temp_ant3)
    time.sleep(1800)

