import sqlite3
from sqlite3.dbapi2 import Cursor
from datetime import date



#data_atual = datetime.datetime.now()
data_atual = date.today()

#FUNÇÕES DE PACIENTES
def buscar_pacientes():
    status = 'Baixado'
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM pacientes WHERE Status_paciente=?'
    cur.execute(sql, (status,))
    return cur.fetchall()

def buscar_todas_escalas():
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT ID_escala, Nome_escala FROM Escalas'
    cur.execute(sql)
    return cur.fetchall()

def buscar_escalas_prescritas(id_paciente):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT ID_relacao, Nome_escala FROM Paciente_escala LEFT JOIN Escalas on Escalas.ID_escala = Paciente_escala.ID_escala WHERE ID_paciente =?'
    cur.execute(sql, (id_paciente,))
    return cur.fetchall()


def buscar_escalas_prescritas_paciente(id_paciente):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT Paciente_escala.ID_escala, Nome_escala FROM Paciente_escala LEFT JOIN Escalas on Escalas.ID_escala = Paciente_escala.ID_escala WHERE ID_paciente =?'
    cur.execute(sql, (id_paciente,))
    return cur.fetchall()

def inserir_relacao(id_paciente, id_escala):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'INSERT INTO Paciente_escala VALUES(?, ?, ?)'
    cur.execute(sql, (None, id_paciente, id_escala))
    banco.commit()
    banco.close()

def busca_relacao_paciente_escala(id_paciente, id_escala):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'SELECT * FROM Paciente_escala WHERE ID_paciente=? AND ID_escala=?'
    cur.execute(sql, (id_paciente, id_escala))
    return cur.fetchone()

def excluir_relacao(id_relacao):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    sql = 'DELETE FROM Paciente_escala WHERE ID_relacao=?'
    cur.execute(sql, (id_relacao,))
    banco.commit()
    banco.close()