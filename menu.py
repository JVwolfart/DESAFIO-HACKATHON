import sqlite3
import sys
from PyQt5 import uic, QtWidgets
import banco
from PyQt5.QtWidgets import QMessageBox
from datetime import date, datetime, time, timedelta
from PyQt5.QtCore import QVariant
from classes import Escala, Paciente
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


def carrega_tabelas_prescricao():
    prescricoes.InputId.setValue(paciente_selecionado.id)
    prescricoes.Nome.setText(paciente_selecionado.nome)
    prescricoes.Prontuario.setText(paciente_selecionado.prontuario)
    serv = banco.buscar_todas_escalas()
    tabela = prescricoes.TabelaEscalas
    row = 0
    tabela.setRowCount(len(serv))
    tabela.setColumnWidth(0, 100)
    tabela.setColumnWidth(1, 100)
    
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in serv:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        row += 1

    escalas_prescritas = banco.buscar_escalas_prescritas(paciente_selecionado.id)
    tabela_prescritas = prescricoes.TabelaPrescricao
    linha = 0
    tabela_prescritas.setRowCount(len(escalas_prescritas))
    tabela_prescritas.setColumnWidth(0, 100)
    tabela_prescritas.setColumnWidth(1, 100)
    tabela_prescritas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela_prescritas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for i in escalas_prescritas:
        tabela_prescritas.setItem(linha, 0, QtWidgets.QTableWidgetItem(f'{i[0]}'))
        tabela_prescritas.setItem(linha, 1, QtWidgets.QTableWidgetItem(f'{i[1]}'))
        linha += 1
    prescricoes.show()

    
def prescrever_escalas():
    linha = prescricoes.TabelaEscalas.currentRow()
    id_escala = int(prescricoes.TabelaEscalas.item(linha, 0).text())
    busca = banco.busca_relacao_paciente_escala(paciente_selecionado.id, id_escala)
    if busca != None:
        QMessageBox.about(prescricoes, 'ERRO', f'O paciente {paciente_selecionado.nome} já possui essa escala prescrita, confira na tabela ao lado')
    else:
        banco.inserir_relacao(paciente_selecionado.id, id_escala)
        carrega_tabelas_prescricao()
    

def excluir_prescricao():
    linha = prescricoes.TabelaPrescricao.currentRow()
    id_relacao = int(prescricoes.TabelaPrescricao.item(linha, 0).text())
    men = QMessageBox.question(prescricoes, 'EXCLUIR PRESCRIÇÃO', f'ATENÇÃO, deseja realmente excluir a prescrição do paciente {paciente_selecionado.nome}?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
    if men == QMessageBox.Ok:
         banco.excluir_relacao(id_relacao)
         carrega_tabelas_prescricao()
        
    else:
        return


def carrega_tabela_afericoes():
    afericoes.InputId.setValue(paciente_selecionado.id)
    afericoes.Nome.setText(paciente_selecionado.nome)
    afericoes.Prontuario.setText(paciente_selecionado.prontuario)
    serv = banco.buscar_escalas_prescritas_paciente(paciente_selecionado.id)
    tabela = afericoes.TabelaEscalas
    row = 0
    tabela.setRowCount(len(serv))
    tabela.setColumnWidth(0, 100)
    tabela.setColumnWidth(1, 100)
    
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in serv:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        row += 1
    afericoes.show()

if __name__ == '__main__':
    paciente_selecionado = Paciente()
    escala_selecionada = Escala()

    qt = QtWidgets.QApplication(sys.argv)
    
    menu = uic.loadUi('enfermagem.ui')
    menu_escalas = uic.loadUi('menu_escalas.ui')
    pacientes = uic.loadUi('pacientes.ui')
    menu_paciente = uic.loadUi('menu_paciente.ui')
    menu_cadastros = uic.loadUi('menu_cadastros.ui')
    prescricoes = uic.loadUi('prescricoes.ui')
    afericoes = uic.loadUi('afericoes.ui')

    ##BOTÕES MENU
    menu.Btn_escalas.clicked.connect(menu_escalas.show)
    menu.Btn_Sair.clicked.connect(menu.close)
    menu.Btn_paciente.clicked.connect(carrega_pacientes)
    pacientes.TabelaPacientes.doubleClicked.connect(pega_paciente)
    menu.Btn_cadastro.clicked.connect(menu_cadastros.show)
    menu_paciente.Btn_prescricao.clicked.connect(carrega_tabelas_prescricao)
    menu_paciente.Btn_afericao.clicked.connect(carrega_tabela_afericoes)
    prescricoes.BtnSair.clicked.connect(prescricoes.close)
    prescricoes.TabelaEscalas.doubleClicked.connect(prescrever_escalas)
    prescricoes.TabelaPrescricao.doubleClicked.connect(excluir_prescricao)
    #menu.showMaximized()
    menu.showMaximized()
    #banco.cria_tabelas()
    qt.exec_()