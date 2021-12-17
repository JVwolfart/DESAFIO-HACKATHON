# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/novas-telas/menu_paciente.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menu_cadastro(object):
    def setupUi(self, menu_cadastro):
        menu_cadastro.setObjectName("menu_cadastro")
        menu_cadastro.setWindowModality(QtCore.Qt.ApplicationModal)
        menu_cadastro.resize(730, 457)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(menu_cadastro.sizePolicy().hasHeightForWidth())
        menu_cadastro.setSizePolicy(sizePolicy)
        menu_cadastro.setMinimumSize(QtCore.QSize(730, 457))
        menu_cadastro.setMaximumSize(QtCore.QSize(730, 457))
        menu_cadastro.setLayoutDirection(QtCore.Qt.LeftToRight)
        menu_cadastro.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        menu_cadastro.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.label = QtWidgets.QLabel(menu_cadastro)
        self.label.setGeometry(QtCore.QRect(50, 170, 121, 91))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.Btn_consulta = QtWidgets.QPushButton(menu_cadastro)
        self.Btn_consulta.setGeometry(QtCore.QRect(40, 60, 132, 88))
        self.Btn_consulta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_consulta.setStyleSheet("QPushButton:hover {   \n"
"    border: 10px solid ;\n"
"    border-color: rgb(0, 112, 179);\n"
"    border-radius: 45px;   \n"
"   \n"
"}\n"
"QPushButton{   \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 45px;\n"
"    border-color: rgb(255, 255, 255);\n"
"}")
        self.Btn_consulta.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/novas-telas/../IMAGENS/icone_consulta.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_consulta.setIcon(icon)
        self.Btn_consulta.setIconSize(QtCore.QSize(120, 100))
        self.Btn_consulta.setObjectName("Btn_consulta")
        self.label_4 = QtWidgets.QLabel(menu_cadastro)
        self.label_4.setGeometry(QtCore.QRect(430, 170, 121, 71))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.Btn_prescricao = QtWidgets.QPushButton(menu_cadastro)
        self.Btn_prescricao.setGeometry(QtCore.QRect(420, 60, 132, 88))
        self.Btn_prescricao.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_prescricao.setStyleSheet("QPushButton:hover {   \n"
"    border: 10px solid ;\n"
"    border-color: rgb(0, 112, 179);\n"
"    border-radius: 45px;   \n"
"   \n"
"}\n"
"QPushButton{   \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 45px;\n"
"    border-color: rgb(255, 255, 255);\n"
"}")
        self.Btn_prescricao.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/novas-telas/../IMAGENS/prescricao_de_escalas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_prescricao.setIcon(icon1)
        self.Btn_prescricao.setIconSize(QtCore.QSize(120, 100))
        self.Btn_prescricao.setObjectName("Btn_prescricao")
        self.label_5 = QtWidgets.QLabel(menu_cadastro)
        self.label_5.setGeometry(QtCore.QRect(240, 170, 111, 71))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.Btn_afericao = QtWidgets.QPushButton(menu_cadastro)
        self.Btn_afericao.setGeometry(QtCore.QRect(230, 60, 132, 88))
        self.Btn_afericao.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_afericao.setAcceptDrops(False)
        self.Btn_afericao.setStyleSheet("QPushButton:hover {   \n"
"    border: 10px solid ;\n"
"    border-color: rgb(0, 112, 179);\n"
"    border-radius: 45px;   \n"
"   \n"
"}\n"
"QPushButton{   \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 45px;\n"
"    border-color: rgb(255, 255, 255);\n"
"}")
        self.Btn_afericao.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/novas-telas/../IMAGENS/cadastro_de_pacientes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_afericao.setIcon(icon2)
        self.Btn_afericao.setIconSize(QtCore.QSize(140, 100))
        self.Btn_afericao.setObjectName("Btn_afericao")
        self.label_7 = QtWidgets.QLabel(menu_cadastro)
        self.label_7.setGeometry(QtCore.QRect(490, 230, 231, 211))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/novas-telas/../IMAGENS/pngwing.com (1).png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(menu_cadastro)
        QtCore.QMetaObject.connectSlotsByName(menu_cadastro)

    def retranslateUi(self, menu_cadastro):
        _translate = QtCore.QCoreApplication.translate
        menu_cadastro.setWindowTitle(_translate("menu_cadastro", "Menu de Paciente"))
        self.label.setText(_translate("menu_cadastro", "Consulta histórico de dados do paciente"))
        self.Btn_consulta.setToolTip(_translate("menu_cadastro", "Consulta histórico de dados do paciente"))
        self.label_4.setText(_translate("menu_cadastro", "Prescrição de escalas"))
        self.Btn_prescricao.setToolTip(_translate("menu_cadastro", "Prescrição de Escalas"))
        self.label_5.setText(_translate("menu_cadastro", "Aferição de escalas do paciente"))
        self.Btn_afericao.setToolTip(_translate("menu_cadastro", "Aferição de escalas do paciente"))
