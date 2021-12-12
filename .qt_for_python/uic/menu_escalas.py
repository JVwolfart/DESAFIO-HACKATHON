# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/menu_escalas.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menu_cadastro(object):
    def setupUi(self, menu_cadastro):
        menu_cadastro.setObjectName("menu_cadastro")
        menu_cadastro.setWindowModality(QtCore.Qt.ApplicationModal)
        menu_cadastro.resize(639, 529)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(menu_cadastro.sizePolicy().hasHeightForWidth())
        menu_cadastro.setSizePolicy(sizePolicy)
        menu_cadastro.setLayoutDirection(QtCore.Qt.LeftToRight)
        menu_cadastro.setStyleSheet("background-color: rgb(52, 101, 164);")
        menu_cadastro.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.label = QtWidgets.QLabel(menu_cadastro)
        self.label.setGeometry(QtCore.QRect(50, 170, 121, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(menu_cadastro)
        self.label_2.setGeometry(QtCore.QRect(270, 170, 111, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.Btn_braden = QtWidgets.QPushButton(menu_cadastro)
        self.Btn_braden.setGeometry(QtCore.QRect(260, 60, 132, 88))
        self.Btn_braden.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_braden.setStyleSheet("QPushButton:hover {   \n"
"    border: 20px solid yellow;\n"
"    background-color: yellow;\n"
"    border-radius: 45px;   \n"
"   \n"
"}\n"
"QPushButton{   \n"
"    background-color:rgb(238, 238, 236);\n"
"}")
        self.Btn_braden.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/IMAGENS/escala de braden.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_braden.setIcon(icon)
        self.Btn_braden.setIconSize(QtCore.QSize(140, 100))
        self.Btn_braden.setObjectName("Btn_braden")
        self.Btn_nhiss = QtWidgets.QPushButton(menu_cadastro)
        self.Btn_nhiss.setGeometry(QtCore.QRect(40, 60, 132, 88))
        self.Btn_nhiss.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_nhiss.setStyleSheet("QPushButton:hover {   \n"
"    border: 20px solid yellow;\n"
"    border-radius: 45px;   \n"
"   \n"
"}\n"
"QPushButton{   \n"
"    background-color:rgb(238, 238, 236);\n"
"}")
        self.Btn_nhiss.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/IMAGENS/AVC.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_nhiss.setIcon(icon1)
        self.Btn_nhiss.setIconSize(QtCore.QSize(120, 100))
        self.Btn_nhiss.setObjectName("Btn_nhiss")
        self.label_3 = QtWidgets.QLabel(menu_cadastro)
        self.label_3.setGeometry(QtCore.QRect(270, 360, 111, 91))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.Btn_richmond = QtWidgets.QPushButton(menu_cadastro)
        self.Btn_richmond.setGeometry(QtCore.QRect(260, 270, 132, 88))
        self.Btn_richmond.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_richmond.setStyleSheet("QPushButton:hover {   \n"
"    border: 20px solid yellow;\n"
"    background-color: yellow;\n"
"    border-radius: 45px;   \n"
"   \n"
"}\n"
"QPushButton{   \n"
"    background-color:rgb(238, 238, 236);\n"
"}")
        self.Btn_richmond.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/IMAGENS/richmond.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_richmond.setIcon(icon2)
        self.Btn_richmond.setIconSize(QtCore.QSize(140, 100))
        self.Btn_richmond.setObjectName("Btn_richmond")
        self.label_4 = QtWidgets.QLabel(menu_cadastro)
        self.label_4.setGeometry(QtCore.QRect(50, 380, 121, 41))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.Btn_ramsay = QtWidgets.QPushButton(menu_cadastro)
        self.Btn_ramsay.setGeometry(QtCore.QRect(40, 270, 132, 88))
        self.Btn_ramsay.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_ramsay.setStyleSheet("QPushButton:hover {   \n"
"    border: 20px solid yellow;\n"
"    border-radius: 45px;   \n"
"   \n"
"}\n"
"QPushButton{   \n"
"    background-color:rgb(238, 238, 236);\n"
"}")
        self.Btn_ramsay.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/IMAGENS/ramsay.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_ramsay.setIcon(icon3)
        self.Btn_ramsay.setIconSize(QtCore.QSize(120, 100))
        self.Btn_ramsay.setObjectName("Btn_ramsay")
        self.label_5 = QtWidgets.QLabel(menu_cadastro)
        self.label_5.setGeometry(QtCore.QRect(450, 170, 111, 41))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.Btn_glassgow = QtWidgets.QPushButton(menu_cadastro)
        self.Btn_glassgow.setGeometry(QtCore.QRect(440, 60, 132, 88))
        self.Btn_glassgow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_glassgow.setStyleSheet("QPushButton:hover {   \n"
"    border: 20px solid yellow;\n"
"    background-color: yellow;\n"
"    border-radius: 45px;   \n"
"   \n"
"}\n"
"QPushButton{   \n"
"    background-color:rgb(238, 238, 236);\n"
"}")
        self.Btn_glassgow.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/IMAGENS/glassgow.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_glassgow.setIcon(icon4)
        self.Btn_glassgow.setIconSize(QtCore.QSize(140, 100))
        self.Btn_glassgow.setObjectName("Btn_glassgow")
        self.Btn_dor = QtWidgets.QPushButton(menu_cadastro)
        self.Btn_dor.setGeometry(QtCore.QRect(430, 270, 132, 88))
        self.Btn_dor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_dor.setStyleSheet("QPushButton:hover {   \n"
"    border: 20px solid yellow;\n"
"    background-color: yellow;\n"
"    border-radius: 45px;   \n"
"   \n"
"}\n"
"QPushButton{   \n"
"    background-color:rgb(238, 238, 236);\n"
"}")
        self.Btn_dor.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("/home/joaovitorwolfart/Dropbox/DESAFIO HACKATHON/IMAGENS/escala_de_dor.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_dor.setIcon(icon5)
        self.Btn_dor.setIconSize(QtCore.QSize(140, 100))
        self.Btn_dor.setObjectName("Btn_dor")
        self.label_6 = QtWidgets.QLabel(menu_cadastro)
        self.label_6.setGeometry(QtCore.QRect(440, 380, 111, 41))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(menu_cadastro)
        QtCore.QMetaObject.connectSlotsByName(menu_cadastro)

    def retranslateUi(self, menu_cadastro):
        _translate = QtCore.QCoreApplication.translate
        menu_cadastro.setWindowTitle(_translate("menu_cadastro", "Menu de Escalas"))
        self.label.setText(_translate("menu_cadastro", "Escala de Nhiss"))
        self.label_2.setText(_translate("menu_cadastro", "Escala de Braden"))
        self.Btn_braden.setToolTip(_translate("menu_cadastro", "Escala Braden"))
        self.Btn_nhiss.setToolTip(_translate("menu_cadastro", "Escala Nhiss"))
        self.label_3.setText(_translate("menu_cadastro", "Escala de Richmond (RASS)"))
        self.Btn_richmond.setToolTip(_translate("menu_cadastro", "Escala Richmond (RASS)"))
        self.label_4.setText(_translate("menu_cadastro", "Escala de Ramsay"))
        self.Btn_ramsay.setToolTip(_translate("menu_cadastro", "Escala de Ramsay"))
        self.label_5.setText(_translate("menu_cadastro", "Escala de Glassgow"))
        self.Btn_glassgow.setToolTip(_translate("menu_cadastro", "Escala de Glassgow"))
        self.Btn_dor.setToolTip(_translate("menu_cadastro", "Escala de Dor"))
        self.label_6.setText(_translate("menu_cadastro", "Escala de dor"))
