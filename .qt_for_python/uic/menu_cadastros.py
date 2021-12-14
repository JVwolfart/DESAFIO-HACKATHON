# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jrwolfart/projetos python jv/DESAFIO-HACKATHON/menu_cadastros.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menu_cadastro(object):
    def setupUi(self, menu_cadastro):
        menu_cadastro.setObjectName("menu_cadastro")
        menu_cadastro.setWindowModality(QtCore.Qt.ApplicationModal)
        menu_cadastro.resize(430, 529)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(menu_cadastro.sizePolicy().hasHeightForWidth())
        menu_cadastro.setSizePolicy(sizePolicy)
        menu_cadastro.setLayoutDirection(QtCore.Qt.LeftToRight)
        menu_cadastro.setStyleSheet("background-color: rgb(52, 101, 164);")
        menu_cadastro.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.label = QtWidgets.QLabel(menu_cadastro)
        self.label.setGeometry(QtCore.QRect(50, 170, 121, 71))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.Btn_cad_usuarios = QtWidgets.QPushButton(menu_cadastro)
        self.Btn_cad_usuarios.setGeometry(QtCore.QRect(40, 60, 132, 88))
        self.Btn_cad_usuarios.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_cad_usuarios.setStyleSheet("QPushButton:hover {   \n"
"    border: 20px solid yellow;\n"
"    border-radius: 45px;   \n"
"   \n"
"}\n"
"QPushButton{   \n"
"    background-color:rgb(238, 238, 236);\n"
"}")
        self.Btn_cad_usuarios.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/jrwolfart/projetos python jv/DESAFIO-HACKATHON/IMAGENS/cadasro_usuario_adobespark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_cad_usuarios.setIcon(icon)
        self.Btn_cad_usuarios.setIconSize(QtCore.QSize(120, 100))
        self.Btn_cad_usuarios.setObjectName("Btn_cad_usuarios")
        self.label_3 = QtWidgets.QLabel(menu_cadastro)
        self.label_3.setGeometry(QtCore.QRect(50, 370, 111, 91))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.Btn_cad_escalas = QtWidgets.QPushButton(menu_cadastro)
        self.Btn_cad_escalas.setGeometry(QtCore.QRect(40, 280, 132, 88))
        self.Btn_cad_escalas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_cad_escalas.setStyleSheet("QPushButton:hover {   \n"
"    border: 20px solid yellow;\n"
"    background-color: yellow;\n"
"    border-radius: 45px;   \n"
"   \n"
"}\n"
"QPushButton{   \n"
"    background-color:rgb(238, 238, 236);\n"
"}")
        self.Btn_cad_escalas.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/jrwolfart/projetos python jv/DESAFIO-HACKATHON/IMAGENS/cadastro_de_escalas.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_cad_escalas.setIcon(icon1)
        self.Btn_cad_escalas.setIconSize(QtCore.QSize(140, 100))
        self.Btn_cad_escalas.setObjectName("Btn_cad_escalas")
        self.label_5 = QtWidgets.QLabel(menu_cadastro)
        self.label_5.setGeometry(QtCore.QRect(220, 170, 111, 41))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.Btn_cad_pacientes = QtWidgets.QPushButton(menu_cadastro)
        self.Btn_cad_pacientes.setGeometry(QtCore.QRect(210, 60, 132, 88))
        self.Btn_cad_pacientes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_cad_pacientes.setAcceptDrops(False)
        self.Btn_cad_pacientes.setStyleSheet("QPushButton:hover {   \n"
"    border: 20px solid yellow;\n"
"    background-color: yellow;\n"
"    border-radius: 45px;   \n"
"   \n"
"}\n"
"QPushButton{   \n"
"    background-color:rgb(238, 238, 236);\n"
"}")
        self.Btn_cad_pacientes.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/jrwolfart/projetos python jv/DESAFIO-HACKATHON/IMAGENS/cadastro_de_pacientes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_cad_pacientes.setIcon(icon2)
        self.Btn_cad_pacientes.setIconSize(QtCore.QSize(140, 100))
        self.Btn_cad_pacientes.setObjectName("Btn_cad_pacientes")
        self.Btn_cad_conceitos = QtWidgets.QPushButton(menu_cadastro)
        self.Btn_cad_conceitos.setGeometry(QtCore.QRect(210, 280, 132, 88))
        self.Btn_cad_conceitos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_cad_conceitos.setStyleSheet("QPushButton:hover {   \n"
"    border: 20px solid yellow;\n"
"    background-color: yellow;\n"
"    border-radius: 45px;   \n"
"   \n"
"}\n"
"QPushButton{   \n"
"    background-color:rgb(238, 238, 236);\n"
"}")
        self.Btn_cad_conceitos.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/home/jrwolfart/projetos python jv/DESAFIO-HACKATHON/IMAGENS/cadastro_de_conceitos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_cad_conceitos.setIcon(icon3)
        self.Btn_cad_conceitos.setIconSize(QtCore.QSize(120, 100))
        self.Btn_cad_conceitos.setObjectName("Btn_cad_conceitos")
        self.label_6 = QtWidgets.QLabel(menu_cadastro)
        self.label_6.setGeometry(QtCore.QRect(220, 390, 111, 61))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(menu_cadastro)
        QtCore.QMetaObject.connectSlotsByName(menu_cadastro)

    def retranslateUi(self, menu_cadastro):
        _translate = QtCore.QCoreApplication.translate
        menu_cadastro.setWindowTitle(_translate("menu_cadastro", "Menu de Cadastros"))
        self.label.setText(_translate("menu_cadastro", "Cadastro de usuários/funcionários"))
        self.Btn_cad_usuarios.setToolTip(_translate("menu_cadastro", "Cadastro de usuários"))
        self.label_3.setText(_translate("menu_cadastro", "Cadastro de escalas"))
        self.Btn_cad_escalas.setToolTip(_translate("menu_cadastro", "Cadastro de escalas"))
        self.label_5.setText(_translate("menu_cadastro", "Cadastro de pacientes"))
        self.Btn_cad_pacientes.setToolTip(_translate("menu_cadastro", "Cadastro de pacientes"))
        self.Btn_cad_conceitos.setToolTip(_translate("menu_cadastro", "Cadastro de Conceitos"))
        self.label_6.setText(_translate("menu_cadastro", "Cadastro de conceitos de escalas"))
