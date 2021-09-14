# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_forno.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 624)
        font = QtGui.QFont()
        font.setPointSize(30)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(49, 54, 59);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMinimumSize(QtCore.QSize(350, 500))
        self.frame_4.setMaximumSize(QtCore.QSize(350, 500))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
        self.frame_3.setMinimumSize(QtCore.QSize(350, 500))
        self.frame_3.setMaximumSize(QtCore.QSize(350, 500))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(0, 10, 350, 50))
        self.label.setMinimumSize(QtCore.QSize(330, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(80, 138, 32);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_1.setGeometry(QtCore.QRect(85, 70, 180, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setMinimumSize(QtCore.QSize(180, 80))
        self.lineEdit_1.setMaximumSize(QtCore.QSize(180, 80))
        font = QtGui.QFont()
        font.setPointSize(44)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setStyleSheet("color: rgb(97, 99, 101);\n"
"background-color: rgb(35, 38, 41);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 7px;\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit_1.setText("")
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(0, 160, 350, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(80, 138, 32);")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(85, 220, 180, 80))
        self.lineEdit_2.setMinimumSize(QtCore.QSize(180, 80))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(180, 80))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: rgb(97, 99, 101);\n"
"background-color: rgb(35, 38, 41);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 7px;\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(85, 400, 180, 80))
        self.lineEdit_4.setMinimumSize(QtCore.QSize(180, 80))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(180, 80))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("color: rgb(97, 99, 101);\n"
"background-color: rgb(35, 38, 41);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 7px;\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(85, 310, 180, 80))
        self.lineEdit_3.setMinimumSize(QtCore.QSize(180, 80))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(180, 80))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("color: rgb(97, 99, 101);\n"
"background-color: rgb(35, 38, 41);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 7px;\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(350, 100))
        self.frame.setMaximumSize(QtCore.QSize(350, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_temp_at = QtWidgets.QPushButton(self.frame)
        self.bt_temp_at.setMinimumSize(QtCore.QSize(180, 80))
        self.bt_temp_at.setMaximumSize(QtCore.QSize(180, 80))
        font = QtGui.QFont()
        font.setPointSize(31)
        font.setBold(True)
        font.setWeight(75)
        self.bt_temp_at.setFont(font)
        self.bt_temp_at.setStyleSheet("background-color: rgb(69, 73, 78);\n"
"color: rgb(80, 138, 32);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 7px;\n"
"border-color: rgb(84, 87, 92);")
        self.bt_temp_at.setObjectName("bt_temp_at")
        self.horizontalLayout.addWidget(self.bt_temp_at)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TEMPERATURA ATUAL (°C)"))
        self.label_2.setText(_translate("MainWindow", "HISTÓRICO DE MEDIÇÕES (°C)"))
        self.bt_temp_at.setText(_translate("MainWindow", "TEMP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

