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
    #if temp > temp_ant and temp > 100:
        #print("ligar nitrogenio")
    #if temp < temp_ant and temp < 300:
        #print("desligar nitrogenio")
    BancoDados().incluir("Dublin", temp)
    time.sleep(1800)

