# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/novas-telas/afericoes.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1036, 820)
        MainWindow.setMinimumSize(QtCore.QSize(1036, 820))
        MainWindow.setMaximumSize(QtCore.QSize(1036, 975))
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BtnSair = QtWidgets.QPushButton(self.centralwidget)
        self.BtnSair.setGeometry(QtCore.QRect(880, 80, 111, 41))
        self.BtnSair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnSair.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(204, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.BtnSair.setObjectName("BtnSair")
        self.InputId = QtWidgets.QSpinBox(self.centralwidget)
        self.InputId.setEnabled(False)
        self.InputId.setGeometry(QtCore.QRect(20, 80, 181, 41))
        self.InputId.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(0, 122, 194);")
        self.InputId.setReadOnly(True)
        self.InputId.setObjectName("InputId")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 171, 22))
        self.label.setObjectName("label")
        self.Nome = QtWidgets.QLineEdit(self.centralwidget)
        self.Nome.setEnabled(True)
        self.Nome.setGeometry(QtCore.QRect(20, 180, 831, 41))
        self.Nome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(0, 122, 194);")
        self.Nome.setReadOnly(True)
        self.Nome.setObjectName("Nome")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 171, 22))
        self.label_4.setObjectName("label_4")
        self.Prontuario = QtWidgets.QLineEdit(self.centralwidget)
        self.Prontuario.setEnabled(True)
        self.Prontuario.setGeometry(QtCore.QRect(220, 80, 631, 41))
        self.Prontuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(0, 122, 194);")
        self.Prontuario.setReadOnly(True)
        self.Prontuario.setObjectName("Prontuario")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 50, 211, 22))
        self.label_3.setObjectName("label_3")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 230, 641, 571))
        self.frame_3.setStyleSheet("background-color: rgb(41, 144, 204);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(100, 30, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.TabelaEscalas = QtWidgets.QTableWidget(self.frame_3)
        self.TabelaEscalas.setEnabled(True)
        self.TabelaEscalas.setGeometry(QtCore.QRect(20, 140, 601, 401))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabelaEscalas.sizePolicy().hasHeightForWidth())
        self.TabelaEscalas.setSizePolicy(sizePolicy)
        self.TabelaEscalas.setMinimumSize(QtCore.QSize(465, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.TabelaEscalas.setFont(font)
        self.TabelaEscalas.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TabelaEscalas.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(138, 226, 52);\n"
"color: rgb(32, 74, 135);")
        self.TabelaEscalas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TabelaEscalas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TabelaEscalas.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.TabelaEscalas.setObjectName("TabelaEscalas")
        self.TabelaEscalas.setColumnCount(2)
        self.TabelaEscalas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaEscalas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TabelaEscalas.setHorizontalHeaderItem(1, item)
        self.TabelaEscalas.horizontalHeader().setDefaultSectionSize(150)
        self.TabelaEscalas.horizontalHeader().setSortIndicatorShown(False)
        self.TabelaEscalas.horizontalHeader().setStretchLastSection(True)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(100, 80, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(730, 470, 251, 241))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/novas-telas/../IMAGENS/pngwing.com (1).png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(230, 0, 551, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aferi????o de escalas de pacientes"))
        self.BtnSair.setText(_translate("MainWindow", "Sair"))
        self.label.setText(_translate("MainWindow", "Id do Paciente"))
        self.Nome.setPlaceholderText(_translate("MainWindow", "Nome do Paciente"))
        self.label_4.setText(_translate("MainWindow", "Nome do paciente"))
        self.Prontuario.setPlaceholderText(_translate("MainWindow", "Prontu??rio do paciente"))
        self.label_3.setText(_translate("MainWindow", "Prontu??rio do Paciente"))
        self.label_6.setText(_translate("MainWindow", "Escalas prescritas para o paciente"))
        self.TabelaEscalas.setSortingEnabled(False)
        item = self.TabelaEscalas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID_escala"))
        item = self.TabelaEscalas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome da escala"))
        self.label_8.setText(_translate("MainWindow", "* D?? um duplo clique na escala para aferir os seus conceitos"))
        self.label_9.setText(_translate("MainWindow", "Aferi????es"))
