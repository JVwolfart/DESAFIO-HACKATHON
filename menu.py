import sqlite3
import sys
from PyQt5 import uic, QtWidgets
import banco
from PyQt5.QtWidgets import QMessageBox
from datetime import date, datetime, time, timedelta
from PyQt5.QtCore import QVariant
from classes import Paciente
#import funcoes

def teste():
    QMessageBox.about(menu, 'Tudo OK', 'Tudo Ok até aqui, mas falta implementar')

data_atual = date.today()
hora = datetime.now().time()
## TESTE

def carrega_pacientes():
    serv = banco.buscar_pacientes()
    tabela = pacientes.TabelaPacientes
    row = 0
    tabela.setRowCount(len(serv))
    tabela.setColumnWidth(0, 70)
    tabela.setColumnWidth(1, 100)
    tabela.setColumnWidth(2, 300)
    tabela.setColumnWidth(3, 100)
    
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in serv:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        row += 1
    pacientes.show()

def pega_paciente():
    linha = pacientes.TabelaPacientes.currentRow()
    paciente_selecionado.id = int(pacientes.TabelaPacientes.item(linha, 0).text())
    paciente_selecionado.nome = pacientes.TabelaPacientes.item(linha, 2).text()
    paciente_selecionado.prontuario = pacientes.TabelaPacientes.item(linha, 1).text()
    paciente_selecionado.status = pacientes.TabelaPacientes.item(linha, 3).text()
    menu_paciente.show()
    
if __name__ == '__main__':
    paciente_selecionado = Paciente()

    qt = QtWidgets.QApplication(sys.argv)
    
    menu = uic.loadUi('enfermagem.ui')
    menu_escalas = uic.loadUi('menu_escalas.ui')
    pacientes = uic.loadUi('pacientes.ui')
    menu_paciente = uic.loadUi('menu_paciente.ui')
    menu_cadastros = uic.loadUi('menu_cadastros.ui')


    ##BOTÕES MENU
    menu.Btn_escalas.clicked.connect(menu_escalas.show)
    menu.Btn_Sair.clicked.connect(menu.close)
    menu.Btn_paciente.clicked.connect(carrega_pacientes)
    pacientes.TabelaPacientes.doubleClicked.connect(pega_paciente)
    menu.Btn_cadastro.clicked.connect(menu_cadastros.show)
    #menu.showMaximized()
    menu.showMaximized()
    #banco.cria_tabelas()
    qt.exec_()