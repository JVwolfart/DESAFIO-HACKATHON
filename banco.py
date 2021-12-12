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