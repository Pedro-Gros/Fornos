import time
import threading
from Utilitarios import Temperatura
from bd import BancoDados
from PyQt5 import QtWidgets, uic

def atualiza():
    while True:
        time.sleep(2)
        temp = Temperatura.temp()
        temps_ant = BancoDados().consulta()
        temp_ant = temps_ant[0][0]
        temp_ant2 = temps_ant[1][0]
        temp_ant3 = temps_ant[2][0]
        tela.lineEdit_1.setText(str(temp))
        tela.lineEdit_2.setText(str(temp_ant))
        tela.lineEdit_3.setText(str(temp_ant2))
        tela.lineEdit_4.setText(str(temp_ant3))

app = QtWidgets.QApplication([])
tela = uic.loadUi("tela_forno.ui")
threading.Thread(target=atualiza).start()
tela.show()
app.exec()