# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/enfermagem.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Janela_principal(object):
    def setupUi(self, Janela_principal):
        Janela_principal.setObjectName("Janela_principal")
        Janela_principal.setWindowModality(QtCore.Qt.NonModal)
        Janela_principal.resize(962, 723)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Janela_principal.sizePolicy().hasHeightForWidth())
        Janela_principal.setSizePolicy(sizePolicy)
        Janela_principal.setMinimumSize(QtCore.QSize(800, 600))
        Janela_principal.setStyleSheet("background-color: rgb(62, 132, 238);")
        self.centralwidget = QtWidgets.QWidget(Janela_principal)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_2.setStyleSheet("background-color: rgb(62, 132, 238);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.Btn_cadastro = QtWidgets.QPushButton(self.frame_2)
        self.Btn_cadastro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_cadastro.setStyleSheet("QPushButton:hover {   \n"
"    border: 20px solid yellow;\n"
"    border-radius: 45px;   \n"
"   \n"
"}\n"
"QPushButton{   \n"
"    background-color:rgb(238, 238, 236);\n"
"}")
        self.Btn_cadastro.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/IMAGENS/cadastro.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_cadastro.setIcon(icon)
        self.Btn_cadastro.setIconSize(QtCore.QSize(100, 100))
        self.Btn_cadastro.setObjectName("Btn_cadastro")
        self.verticalLayout_2.addWidget(self.Btn_cadastro)
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.Btn_escalas = QtWidgets.QPushButton(self.frame_2)
        self.Btn_escalas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_escalas.setStyleSheet("QPushButton:hover {   \n"
"    border: 20px solid yellow;\n"
"    border-radius: 45px;   \n"
"   \n"
"}\n"
"QPushButton{   \n"
"    background-color:rgb(238, 238, 236);\n"
"}")
        self.Btn_escalas.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/IMAGENS/icone_escala.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_escalas.setIcon(icon1)
        self.Btn_escalas.setIconSize(QtCore.QSize(120, 100))
        self.Btn_escalas.setObjectName("Btn_escalas")
        self.verticalLayout_2.addWidget(self.Btn_escalas)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.Btn_paciente = QtWidgets.QPushButton(self.frame_2)
        self.Btn_paciente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_paciente.setStyleSheet("QPushButton:hover {   \n"
"    border: 20px solid yellow;\n"
"    background-color: yellow;\n"
"    border-radius: 45px;   \n"
"   \n"
"}\n"
"QPushButton{   \n"
"    background-color:rgb(238, 238, 236);\n"
"}")
        self.Btn_paciente.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/IMAGENS/1100026-homem-em-on-line-consulta-de-saude-com-doutor-em-computador-laptop-isometrico-kit-medico-vetor.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_paciente.setIcon(icon2)
        self.Btn_paciente.setIconSize(QtCore.QSize(180, 100))
        self.Btn_paciente.setObjectName("Btn_paciente")
        self.verticalLayout_2.addWidget(self.Btn_paciente)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.Btn_Sair = QtWidgets.QPushButton(self.frame_2)
        self.Btn_Sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_Sair.setStyleSheet("QPushButton:hover {   \n"
"    border: 20px solid yellow;\n"
"    border-radius: 45px;   \n"
"   \n"
"}\n"
"QPushButton{   \n"
"    background-color:rgb(238, 238, 236);\n"
"}")
        self.Btn_Sair.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/IMAGENS/Sair do sistema_adobespark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Sair.setIcon(icon3)
        self.Btn_Sair.setIconSize(QtCore.QSize(100, 100))
        self.Btn_Sair.setObjectName("Btn_Sair")
        self.verticalLayout_2.addWidget(self.Btn_Sair)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/IMAGENS/20200902_enfermagem.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame)
        Janela_principal.setCentralWidget(self.centralwidget)
        self.actionProdutos = QtWidgets.QAction(Janela_principal)
        self.actionProdutos.setObjectName("actionProdutos")
        self.actionUsuarios = QtWidgets.QAction(Janela_principal)
        self.actionUsuarios.setObjectName("actionUsuarios")
        self.actionPedidos = QtWidgets.QAction(Janela_principal)
        self.actionPedidos.setObjectName("actionPedidos")
        self.actionTrocar = QtWidgets.QAction(Janela_principal)
        self.actionTrocar.setObjectName("actionTrocar")
        self.actionMudar_Usuario = QtWidgets.QAction(Janela_principal)
        self.actionMudar_Usuario.setObjectName("actionMudar_Usuario")
        self.actionSair = QtWidgets.QAction(Janela_principal)
        self.actionSair.setObjectName("actionSair")

        self.retranslateUi(Janela_principal)
        QtCore.QMetaObject.connectSlotsByName(Janela_principal)

    def retranslateUi(self, Janela_principal):
        _translate = QtCore.QCoreApplication.translate
        Janela_principal.setWindowTitle(_translate("Janela_principal", "Desafio de Ambiente e Saúde Para o Hackathon Jovem Programador"))
        self.Btn_cadastro.setToolTip(_translate("Janela_principal", "Abre o Menu de Cadastros"))
        self.label.setText(_translate("Janela_principal", "Cadastros"))
        self.Btn_escalas.setToolTip(_translate("Janela_principal", "Menu de Escalas"))
        self.label_5.setText(_translate("Janela_principal", "Escalas"))
        self.Btn_paciente.setToolTip(_translate("Janela_principal", "Informações dos pacientes"))
        self.label_8.setText(_translate("Janela_principal", "Selecionar pacientes"))
        self.Btn_Sair.setToolTip(_translate("Janela_principal", "Click aqui para efetuar o Logout"))
        self.label_4.setText(_translate("Janela_principal", "Sair do Sistema"))
        self.actionProdutos.setText(_translate("Janela_principal", "Produtos"))
        self.actionUsuarios.setText(_translate("Janela_principal", "Usuarios"))
        self.actionPedidos.setText(_translate("Janela_principal", "Pedidos"))
        self.actionTrocar.setText(_translate("Janela_principal", "Sair do Sistema"))
        self.actionMudar_Usuario.setText(_translate("Janela_principal", "Mudar Usuario"))
        self.actionSair.setText(_translate("Janela_principal", "Sair"))
