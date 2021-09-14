import threading
import time
import sys

from bd import BancoDados
from Utilitarios import Temperatura
from tela_forno import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog


class tela_forno(QMainWindow):

    def _init_(self, args, *argvs):
        super(tela_forno, self)._init_(args, *argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.bt_temp_at.pressed.connect(self.atualiza)

    def atualiza(self):
        time.sleep(2)
        temp = Temperatura.temp()
        temps_ant = BancoDados().consulta()
        temp_ant = temps_ant[0][0]
        temp_ant2 = temps_ant[1][0]
        temp_ant3 = temps_ant[2][0]
        self.ui.lineEdit.setText(str(temp))
        self.ui.lineEdit_2.setText(str(temp_ant))
        self.ui.lineEdit_3.setText(str(temp_ant2))
        self.ui.lineEdit_4.setText(str(temp_ant3))




app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = tela_forno()
    window.show()
#threading.Thread(target= tela_forno.atualiza).start()
sys.exit(app.exec_())


