# Importação de Lib
import seaborn as sns
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import sqlite3
import matplotlib
from matplotlib import style
from datetime import datetime
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
import random
import scipy.stats as st
from scipy.stats import norm
import pandas as pd 
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import*
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
import coletabeta
from datetime import datetime
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,  QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import Qt
import sqlite3
from PyQt5.QtGui import QIcon, QPixmap
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')

#Classe da janela de análise
class imporSA(Qt.QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Análise estatística de fatores'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
   
        self.setWindowTitle(self.title) 
        self.setGeometry(self.left, self.top, self.width, self.height) 
   
        self.createTable() 
   
        self.layout = QVBoxLayout() 
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 

        self.show() 
   
#Criação da tabela
    def createTable(self): 
        self.tableWidget = QTableWidget() 

        self.tableWidget.setRowCount(26)  
  

        self.tableWidget.setColumnCount(2)  

        self.tableWidget.setHorizontalHeaderLabels(('Gráfico da Análise', 'Gráfico Normalizado da Análise'))

#Botões dos Gráficos Normalizados

        btnFN1 = QPushButton(self.tableWidget)
        btnFN1.setText('Gráfico Normalizado 1')
        self.tableWidget.setCellWidget(0,1, btnFN1)
        btnFN1.clicked.connect(self.grafnormF1)

        btnFN2 = QPushButton(self.tableWidget)
        btnFN2.setText('Gráfico Normalizado 2')
        self.tableWidget.setCellWidget(1,1, btnFN2)
        btnFN2.clicked.connect(self.grafnormF2)

        btnFN3 = QPushButton(self.tableWidget)
        btnFN3.setText('Gráfico Normalizado 3')
        self.tableWidget.setCellWidget(2,1, btnFN3)
        btnFN3.clicked.connect(self.grafnormF3)

        btnFN4 = QPushButton(self.tableWidget)
        btnFN4.setText('Gráfico Normalizado 4')
        self.tableWidget.setCellWidget(3,1, btnFN4)
        btnFN4.clicked.connect(self.grafnormF4)

        btnFN5 = QPushButton(self.tableWidget)
        btnFN5.setText('Gráfico Normalizado 5')
        self.tableWidget.setCellWidget(4,1, btnFN5)
        btnFN5.clicked.connect(self.grafnormF5)

        btnFN6 = QPushButton(self.tableWidget)
        btnFN6.setText('Gráfico Normalizado 6')
        self.tableWidget.setCellWidget(5,1, btnFN6)
        btnFN6.clicked.connect(self.grafnormF6)

        btnFN7 = QPushButton(self.tableWidget)
        btnFN7.setText('Gráfico Normalizado 7')
        self.tableWidget.setCellWidget(6,1, btnFN7)
        btnFN7.clicked.connect(self.grafnormF7)

        btnFN8 = QPushButton(self.tableWidget)
        btnFN8.setText('Gráfico Normalizado 8')
        self.tableWidget.setCellWidget(7,1, btnFN8)
        btnFN8.clicked.connect(self.grafnormF8)

        btnFN9 = QPushButton(self.tableWidget)
        btnFN9.setText('Gráfico Normalizado 9')
        self.tableWidget.setCellWidget(8,1, btnFN9)
        btnFN9.clicked.connect(self.grafnormF9)

        btnFN10 = QPushButton(self.tableWidget)
        btnFN10.setText('Gráfico Normalizado 10')
        self.tableWidget.setCellWidget(9,1, btnFN10)
        btnFN10.clicked.connect(self.grafnormF10)

        btnFN11 = QPushButton(self.tableWidget)
        btnFN11.setText('Gráfico Normalizado 11')
        self.tableWidget.setCellWidget(10,1, btnFN11)
        btnFN11.clicked.connect(self.grafnormF11)

        btnFN12 = QPushButton(self.tableWidget)
        btnFN12.setText('Gráfico Normalizado 12')
        self.tableWidget.setCellWidget(11,1, btnFN12)
        btnFN12.clicked.connect(self.grafnormF12)

        btnFN13 = QPushButton(self.tableWidget)
        btnFN13.setText('Gráfico Normalizado 13')
        self.tableWidget.setCellWidget(12,1, btnFN13)
        btnFN13.clicked.connect(self.grafnormF13)

        btnFN14 = QPushButton(self.tableWidget)
        btnFN14.setText('Gráfico Normalizado 14')
        self.tableWidget.setCellWidget(13,1, btnFN14)
        btnFN14.clicked.connect(self.grafnormF14)

        btnFN15 = QPushButton(self.tableWidget)
        btnFN15.setText('Gráfico Normalizado 15')
        self.tableWidget.setCellWidget(14,1, btnFN15)
        btnFN15.clicked.connect(self.grafnormF15)

        btnFN16 = QPushButton(self.tableWidget)
        btnFN16.setText('Gráfico Normalizado 16')
        self.tableWidget.setCellWidget(15,1, btnFN16)
        btnFN16.clicked.connect(self.grafnormF16)

        btnFN17 = QPushButton(self.tableWidget)
        btnFN17.setText('Gráfico Normalizado 17')
        self.tableWidget.setCellWidget(16,1, btnFN17)
        btnFN17.clicked.connect(self.grafnormF17)

        btnFN18 = QPushButton(self.tableWidget)
        btnFN18.setText('Gráfico Normalizado 18')
        self.tableWidget.setCellWidget(17,1, btnFN18)
        btnFN18.clicked.connect(self.grafnormF18)

        btnFN19 = QPushButton(self.tableWidget)
        btnFN19.setText('Gráfico Normalizado 19')
        self.tableWidget.setCellWidget(18,1, btnFN19)
        btnFN19.clicked.connect(self.grafnormF19)

        btnFN20 = QPushButton(self.tableWidget)
        btnFN20.setText('Gráfico Normalizado 20')
        self.tableWidget.setCellWidget(19,1, btnFN20)
        btnFN20.clicked.connect(self.grafnormF20)

        btnFN21 = QPushButton(self.tableWidget)
        btnFN21.setText('Gráfico Normalizado 21')
        self.tableWidget.setCellWidget(20,1, btnFN21)
        btnFN21.clicked.connect(self.grafnormF21)

        btnFN22 = QPushButton(self.tableWidget)
        btnFN22.setText('Gráfico Normalizado 22')
        self.tableWidget.setCellWidget(21,1, btnFN22)
        btnFN22.clicked.connect(self.grafnormF22)

        btnFN23 = QPushButton(self.tableWidget)
        btnFN23.setText('Gráfico Normalizado 23')
        self.tableWidget.setCellWidget(22,1, btnFN23)
        btnFN23.clicked.connect(self.grafnormF23)

        btnFN24 = QPushButton(self.tableWidget)
        btnFN24.setText('Gráfico Normalizado 24')
        self.tableWidget.setCellWidget(23,1, btnFN24)
        btnFN24.clicked.connect(self.grafnormF24)

        btnFN25 = QPushButton(self.tableWidget)
        btnFN25.setText('Gráfico Normalizado 25')
        self.tableWidget.setCellWidget(24,1, btnFN25)
        btnFN25.clicked.connect(self.grafnormF25)

        btnFN26 = QPushButton(self.tableWidget)
        btnFN26.setText('Gráfico Normalizado 26')
        self.tableWidget.setCellWidget(25,1, btnFN26)
        btnFN26.clicked.connect(self.grafnormF26)

#Botões dos Gráficos Nº de análises x fator

        btnF1 = QPushButton(self.tableWidget)
        btnF1.setText('Fator 1')
        self.tableWidget.setCellWidget(0,0, btnF1)
        btnF1.clicked.connect(self.grafF1)

        btnF2 = QPushButton(self.tableWidget)
        btnF2.setText('Fator 2')
        self.tableWidget.setCellWidget(1,0, btnF2)
        btnF2.clicked.connect(self.grafF2)

        btnF3 = QPushButton(self.tableWidget)
        btnF3.setText('Fator 3')
        self.tableWidget.setCellWidget(2,0, btnF3)
        btnF3.clicked.connect(self.grafF3)

        btnF4 = QPushButton(self.tableWidget)
        btnF4.setText('Fator 4')
        self.tableWidget.setCellWidget(3,0, btnF4)
        btnF4.clicked.connect(self.grafF4)

        btnF5 = QPushButton(self.tableWidget)
        btnF5.setText('Fator 5')
        self.tableWidget.setCellWidget(4,0, btnF5)
        btnF5.clicked.connect(self.grafF5)

        btnF6 = QPushButton(self.tableWidget)
        btnF6.setText('Fator 6')
        self.tableWidget.setCellWidget(5,0, btnF6)
        btnF6.clicked.connect(self.grafF6)

        btnF7 = QPushButton(self.tableWidget)
        btnF7.setText('Fator 7')
        self.tableWidget.setCellWidget(6,0, btnF7)
        btnF7.clicked.connect(self.grafF7)

        btnF8 = QPushButton(self.tableWidget)
        btnF8.setText('Fator 8')
        self.tableWidget.setCellWidget(7,0, btnF8)
        btnF8.clicked.connect(self.grafF8)

        btnF9 = QPushButton(self.tableWidget)
        btnF9.setText('Fator 9')
        self.tableWidget.setCellWidget(8,0, btnF9)
        btnF9.clicked.connect(self.grafF9)

        btnF10 = QPushButton(self.tableWidget)
        btnF10.setText('Fator 10')
        self.tableWidget.setCellWidget(9,0, btnF10)
        btnF10.clicked.connect(self.grafF10)

        btnF11 = QPushButton(self.tableWidget)
        btnF11.setText('Fator 11')
        self.tableWidget.setCellWidget(10,0, btnF11)
        btnF11.clicked.connect(self.grafF11)

        btnF12 = QPushButton(self.tableWidget)
        btnF12.setText('Fator 12')
        self.tableWidget.setCellWidget(11,0, btnF12)
        btnF12.clicked.connect(self.grafF12)

        btnF13 = QPushButton(self.tableWidget)
        btnF13.setText('Fator 13')
        self.tableWidget.setCellWidget(12,0, btnF13)
        btnF13.clicked.connect(self.grafF13)

        btnF14 = QPushButton(self.tableWidget)
        btnF14.setText('Fator 14')
        self.tableWidget.setCellWidget(13,0, btnF14)
        btnF14.clicked.connect(self.grafF14)

        btnF15 = QPushButton(self.tableWidget)
        btnF15.setText('Fator 15')
        self.tableWidget.setCellWidget(14,0, btnF15)
        btnF15.clicked.connect(self.grafF15)

        btnF16 = QPushButton(self.tableWidget)
        btnF16.setText('Fator 16')
        self.tableWidget.setCellWidget(15,0, btnF16)
        btnF16.clicked.connect(self.grafF16)

        btnF17 = QPushButton(self.tableWidget)
        btnF17.setText('Fator 17')
        self.tableWidget.setCellWidget(16,0, btnF17)
        btnF17.clicked.connect(self.grafF17)

        btnF18 = QPushButton(self.tableWidget)
        btnF18.setText('Fator 18')
        self.tableWidget.setCellWidget(17,0, btnF18)
        btnF18.clicked.connect(self.grafF18)

        btnF19 = QPushButton(self.tableWidget)
        btnF19.setText('Fator 19')
        self.tableWidget.setCellWidget(18,0, btnF19)
        btnF19.clicked.connect(self.grafF19)

        btnF20 = QPushButton(self.tableWidget)
        btnF20.setText('Fator 20')
        self.tableWidget.setCellWidget(19,0, btnF20)
        btnF20.clicked.connect(self.grafF20)

        btnF21 = QPushButton(self.tableWidget)
        btnF21.setText('Fator 21')
        self.tableWidget.setCellWidget(20,0, btnF21)
        btnF21.clicked.connect(self.grafF21)

        btnF22 = QPushButton(self.tableWidget)
        btnF22.setText('Fator 22')
        self.tableWidget.setCellWidget(21,0, btnF22)
        btnF22.clicked.connect(self.grafF22)

        btnF23 = QPushButton(self.tableWidget)
        btnF23.setText('Fator 23')
        self.tableWidget.setCellWidget(22,0, btnF23)
        btnF23.clicked.connect(self.grafF23)

        btnF24 = QPushButton(self.tableWidget)
        btnF24.setText('Fator 24')
        self.tableWidget.setCellWidget(23,0, btnF24)
        btnF24.clicked.connect(self.grafF24)

        btnF25 = QPushButton(self.tableWidget)
        btnF25.setText('Fator 25')
        self.tableWidget.setCellWidget(24,0, btnF25)
        btnF25.clicked.connect(self.grafF25)

        btnF26 = QPushButton(self.tableWidget)
        btnF26.setText('Fator 26')
        self.tableWidget.setCellWidget(25,0, btnF26)
        btnF26.clicked.connect(self.grafF26)


#tableWidget se adequa a janela 
        self.tableWidget.horizontalHeader().setStretchLastSection(True) 
        self.tableWidget.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch) 

#Geração de Gráficos Nº de análise x Fatores
    def grafF1(self): 
        self.label = QLabel()
#Conexão ao banco de dados local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator1 FROM Sa1')
        data = c.fetchall()

        Id = []
        Fator1 = []


        for row in data:
            Id.append(row[0])
            Fator1.append(row[1])

        plt.plot(Id,Fator1,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF2(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator2 FROM Sa1')
        data = c.fetchall()

        Id = []
        Fator2 = []


        for row in data:
            Id.append(row[0])
            Fator2.append(row[1])

        plt.plot(Id,Fator2,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF3(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator3 FROM Sa1')
        data = c.fetchall()

        Id = []
        Fator3 = []


        for row in data:
            Id.append(row[0])
            Fator3.append(row[1])

        plt.plot(Id,Fator3,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF4(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator4 FROM Sa1')
        data = c.fetchall()

        Id = []
        Fator4 = []


        for row in data:
            Id.append(row[0])
            Fator4.append(row[1])

        plt.plot(Id,Fator4,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF5(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator5 FROM Sa1')
        data = c.fetchall()

        Id = []
        Fator5 = []


        for row in data:
            Id.append(row[0])
            Fator5.append(row[1])

        plt.plot(Id,Fator5,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF6(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator6 FROM Sa1')
        data = c.fetchall()

        Id = []
        Fator6 = []


        for row in data:
            Id.append(row[0])
            Fator6.append(row[1])

        plt.plot(Id,Fator6,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF7(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator7 FROM Sa1')
        data = c.fetchall()

        Id = []
        Fator7 = []


        for row in data:
            Id.append(row[0])
            Fator7.append(row[1])

        plt.plot(Id,Fator7,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF8(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator8 FROM Sa1')
        data = c.fetchall()

        Id = []
        Fator8 = []


        for row in data:
            Id.append(row[0])
            Fator8.append(row[1])

        plt.plot(Id,Fator8,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF9(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator9 FROM Sa1')
        data = c.fetchall()

        Id = []
        Fator9 = []


        for row in data:
            Id.append(row[0])
            Fator9.append(row[1])

        plt.plot(Id,Fator9,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF10(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator10 FROM Sa1')
        data = c.fetchall()

        Id = []
        Fator10 = []


        for row in data:
            Id.append(row[0])
            Fator10.append(row[1])

        plt.plot(Id,Fator10,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF11(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator11 FROM Sa1')
        data = c.fetchall()

        Id = []
        Fator11 = []


        for row in data:
            Id.append(row[0])
            Fator11.append(row[1])

        plt.plot(Id,Fator11,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF12(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator12 FROM Sa2')
        data = c.fetchall()

        Id = []
        Fator12 = []


        for row in data:
            Id.append(row[0])
            Fator12.append(row[1])

        plt.plot(Id,Fator12,'-')
        plt.show()

        c.close()
        conn.close()
        
    def grafF13(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator13 FROM Sa2')
        data = c.fetchall()

        Id = []
        Fator13 = []


        for row in data:
            Id.append(row[0])
            Fator13.append(row[1])

        plt.plot(Id,Fator13,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF14(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator14 FROM Sa2')
        data = c.fetchall()

        Id = []
        Fator14 = []


        for row in data:
            Id.append(row[0])
            Fator14.append(row[1])

        plt.plot(Id,Fator14,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF15(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator15 FROM Sa2')
        data = c.fetchall()

        Id = []
        Fator15 = []


        for row in data:
            Id.append(row[0])
            Fator15.append(row[1])

        plt.plot(Id,Fator15,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF16(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator16 FROM Sa2')
        data = c.fetchall()

        Id = []
        Fator16 = []


        for row in data:
            Id.append(row[0])
            Fator16.append(row[1])

        plt.plot(Id,Fator16,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF17(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator17 FROM Sa2')
        data = c.fetchall()

        Id = []
        Fator17 = []


        for row in data:
            Id.append(row[0])
            Fator17.append(row[1])

        plt.plot(Id,Fator17,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF18(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator18 FROM Sa2')
        data = c.fetchall()

        Id = []
        Fator18 = []


        for row in data:
            Id.append(row[0])
            Fator18.append(row[1])

        plt.plot(Id,Fator18,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF19(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator19 FROM Sa2')
        data = c.fetchall()

        Id = []
        Fator19 = []


        for row in data:
            Id.append(row[0])
            Fator19.append(row[1])

        plt.plot(Id,Fator19,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF20(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator20 FROM Sa2')
        data = c.fetchall()

        Id = []
        Fator20 = []


        for row in data:
            Id.append(row[0])
            Fator20.append(row[1])

        plt.plot(Id,Fator20,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF21(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator21 FROM Sa2')
        data = c.fetchall()

        Id = []
        Fator21 = []


        for row in data:
            Id.append(row[0])
            Fator21.append(row[1])

        plt.plot(Id,Fator21,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF22(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator22 FROM Sa2')
        data = c.fetchall()

        Id = []
        Fator22 = []


        for row in data:
            Id.append(row[0])
            Fator22.append(row[1])

        plt.plot(Id,Fator22,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF23(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator23 FROM Sa3')
        data = c.fetchall()

        Id = []
        Fator23 = []


        for row in data:
            Id.append(row[0])
            Fator23.append(row[1])

        plt.plot(Id,Fator23,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF24(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator24 FROM Sa3')
        data = c.fetchall()

        Id = []
        Fator24 = []


        for row in data:
            Id.append(row[0])
            Fator24.append(row[1])

        plt.plot(Id,Fator24,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF25(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator25 FROM Sa3')
        data = c.fetchall()

        Id = []
        Fator25 = []


        for row in data:
            Id.append(row[0])
            Fator25.append(row[1])

        plt.plot(Id,Fator25,'-')
        plt.show()

        c.close()
        conn.close()
        
    def grafF26(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator26 FROM Sa3')
        data = c.fetchall()

        Id = []
        Fator26 = []


        for row in data:
            Id.append(row[0])
            Fator26.append(row[1])

        plt.plot(Id,Fator26,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF27(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator27 FROM Sa3')
        data = c.fetchall()

        Id = []
        Fator27 = []


        for row in data:
            Id.append(row[0])
            Fator27.append(row[1])

        plt.plot(Id,Fator27,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF28(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator28 FROM Sa3')
        data = c.fetchall()

        Id = []
        Fator28 = []


        for row in data:
            Id.append(row[0])
            Fator28.append(row[1])

        plt.plot(Id,Fator28,'-')
        plt.show()

        c.close()
        conn.close()

    def grafF29(self): 
        self.label = QLabel()
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        c.execute('SELECT Id, Fator29 FROM Sa3')
        data = c.fetchall()

        Id = []
        Fator29 = []


        for row in data:
            Id.append(row[0])
            Fator29.append(row[1])

        plt.plot(Id,Fator29,'-')
        plt.show()

        c.close()
        conn.close()

# grafico normalizado 

    def grafnormF1(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator1 FROM Sa1')
        data = np.array(c.fetchall())

        

        ## dados do banco
        Fator1 = []
        for row in result:
            Fator1.append(float(row[1]))
        
        sns.histplot(data,kde=True,stat='probability')

        plt.show()

    def grafnormF2(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator2 FROM Sa1')
        data = np.array(c.fetchall())

        

        ## dados do banco
        Fator2 = []
        for row in result:
            Fator2.append(float(row[1]))
        
        sns.histplot(data,kde=True,stat='probability')

        plt.show()

    def grafnormF3(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator3 FROM Sa1')
        data = np.array(c.fetchall())

        

        ## dados do banco
        Fator3 = []
        for row in result:
            Fator3.append(float(row[1]))
        
        sns.histplot(data,kde=True,stat='probability')

        plt.show()

    def grafnormF4(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator4 FROM Sa1')
        data = np.array(c.fetchall())

        

        ## dados do banco
        Fator4 = []
        for row in result:
            Fator4.append(float(row[1]))
        
        sns.histplot(data,kde=True,stat='probability')

        plt.show()

    def grafnormF4(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator5 FROM Sa1')
        data = np.array(c.fetchall())

        

        ## dados do banco
        Fator5 = []
        for row in result:
            Fator5.append(float(row[1]))
        
        sns.histplot(data,kde=True,stat='probability')

        plt.show()

    def grafnormF5(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator6 FROM Sa1')
        data = np.array(c.fetchall())

        

        ## dados do banco
        Fator6 = []
        for row in result:
            Fator6.append(float(row[1]))
        
        sns.histplot(data,kde=True,stat='probability')

        plt.show()

    def grafnormF6(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator6 FROM Sa1')
        data = np.array(c.fetchall())

        

        ## dados do banco
        Fator6 = []
        for row in result:
            Fator6.append(float(row[1]))
        
        sns.histplot(data,kde=True,stat='probability')

        plt.show()

    def grafnormF7(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator7 FROM Sa1')
        data = np.array(c.fetchall())

        

        ## dados do banco
        Fator7 = []
        for row in result:
            Fator7.append(float(row[1]))
        
        sns.histplot(data,kde=True,stat='probability')

        plt.show()

    def grafnormF8(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator8 FROM Sa1')
        data = np.array(c.fetchall())

        

        ## dados do banco
        Fator8 = []
        for row in result:
            Fator8.append(float(row[1]))
        
        sns.histplot(data,kde=True,stat='probability')

        plt.show()

    def grafnormF9(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator9 FROM Sa1')
        data = np.array(c.fetchall())

        

        ## dados do banco
        Fator9 = []
        for row in result:
            Fator9.append(float(row[1]))
        
        sns.histplot(data,kde=True,stat='probability')

        plt.show()

    def grafnormF10(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator10 FROM Sa1')
        data = np.array(c.fetchall())

        

        ## dados do banco
        Fator10 = []
        for row in result:
            Fator10.append(float(row[1]))
        
        sns.histplot(data,kde=True,stat='probability')

        plt.show()

    def grafnormF11(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator11 FROM Sa1')
        data = np.array(c.fetchall())

        

        ## dados do banco
        Fator11 = []
        for row in result:
            Fator11.append(float(row[1]))
        
        sns.histplot(data,kde=True,stat='probability')

        plt.show()

    def grafnormF12(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator12 FROM Sa2')
        data = np.array(c.fetchall())

        

        ## dados do banco
        x = []
        for i in range(15):
            x.append(eval (data[i][0]))
        
        x = np.array(x)
        
        sns.histplot(x,kde=True,stat='probability')

        plt.show()

    def grafnormF13(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator13 FROM Sa2')
        data = np.array(c.fetchall())

        ## dados do banco
        x = []
        for i in range(15):
            x.append(eval (data[i][0]))
        
        x = np.array(x)
        
        sns.histplot(x,kde=True,stat='probability')

        plt.show()

    def grafnormF14(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator14 FROM Sa2')
        data = np.array(c.fetchall())

        

        ## dados do banco
        x = []
        for i in range(15):
            x.append(eval (data[i][0]))
        
        x = np.array(x)
        
        sns.histplot(x,kde=True,stat='probability')

        plt.show()

    def grafnormF15(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator15 FROM Sa2')
        data = np.array(c.fetchall())

        ## dados do banco
        x = []
        for i in range(15):
            x.append(eval (data[i][0]))
        
        x = np.array(x)
        
        sns.histplot(x,kde=True,stat='probability')

        plt.show()

    def grafnormF16(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator16 FROM Sa2')
        data = np.array(c.fetchall())

        

        ## dados do banco
        x = []
        for i in range(15):
            x.append(eval (data[i][0]))
        
        x = np.array(x)
        
        sns.histplot(x,kde=True,stat='probability')

        plt.show()

    def grafnormF17(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator17 FROM Sa2')
        data = np.array(c.fetchall())

        ## dados do banco
        x = []
        for i in range(15):
            x.append(eval (data[i][0]))
        
        x = np.array(x)
        
        sns.histplot(x,kde=True,stat='probability')

        plt.show()

    def grafnormF18(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator18 FROM Sa2')
        data = np.array(c.fetchall())

        

        ## dados do banco
        x = []
        for i in range(15):
            x.append(eval (data[i][0]))
        
        x = np.array(x)
        
        sns.histplot(x,kde=True,stat='probability')

        plt.show()

    def grafnormF19(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator19 FROM Sa2')
        data = np.array(c.fetchall())

        ## dados do banco
        x = []
        for i in range(15):
            x.append(eval (data[i][0]))
        
        x = np.array(x)
        
        sns.histplot(x,kde=True,stat='probability')

        plt.show()

    def grafnormF20(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator20 FROM Sa2')
        data = np.array(c.fetchall())

        

        ## dados do banco
        x = []
        for i in range(15):
            x.append(eval (data[i][0]))
        
        x = np.array(x)
        
        sns.histplot(x,kde=True,stat='probability')

        plt.show()

    def grafnormF21(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator21 FROM Sa2')
        data = np.array(c.fetchall())

        ## dados do banco
        x = []
        for i in range(15):
            x.append(eval (data[i][0]))
        
        x = np.array(x)
        
        sns.histplot(x,kde=True,stat='probability')

        plt.show()
    
    def grafnormF22(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator22 FROM Sa2')
        data = np.array(c.fetchall())

        

        ## dados do banco
        x = []
        for i in range(15):
            x.append(eval (data[i][0]))
        
        x = np.array(x)
        
        sns.histplot(x,kde=True,stat='probability')

        plt.show()

    def grafnormF23(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator23 FROM Sa3')
        data = np.array(c.fetchall())

        ## dados do banco
        x = []
        for i in range(15):
            x.append(eval (data[i][0]))
        
        x = np.array(x)
        
        sns.histplot(x,kde=True,stat='probability')

        plt.show()

    def grafnormF24(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator24 FROM Sa3')
        data = np.array(c.fetchall())

        

        ## dados do banco
        x = []
        for i in range(15):
            x.append(eval (data[i][0]))
        
        x = np.array(x)
        
        sns.histplot(x,kde=True,stat='probability')

        plt.show()

    def grafnormF25(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator25 FROM Sa3')
        data = np.array(c.fetchall())

        ## dados do banco
        x = []
        for i in range(15):
            x.append(eval (data[i][0]))
        
        x = np.array(x)
        
        sns.histplot(x,kde=True,stat='probability')

        plt.show()

    def grafnormF26(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator26 FROM Sa3')
        data = np.array(c.fetchall())

        

        ## dados do banco
        x = []
        for i in range(15):
            x.append(eval (data[i][0]))
        
        x = np.array(x)
        
        sns.histplot(x,kde=True,stat='probability')

        plt.show()

    def grafnormF27(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator27 FROM Sa3')
        data = np.array(c.fetchall())

        ## dados do banco
        x = []
        for i in range(15):
            x.append(eval (data[i][0]))
        
        x = np.array(x)
        
        sns.histplot(x,kde=True,stat='probability')

        plt.show()

    def grafnormF28(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator28 FROM Sa3')
        data = np.array(c.fetchall())

        ## dados do banco
        x = []
        for i in range(15):
            x.append(eval (data[i][0]))
        
        x = np.array(x)
        
        sns.histplot(x,kde=True,stat='probability')

        plt.show()

    def grafnormF29(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator29 FROM Sa3')
        data = np.array(c.fetchall())

        ## dados do banco
        x = []
        for i in range(15):
            x.append(eval (data[i][0]))
        
        x = np.array(x)
        
        sns.histplot(x,kde=True,stat='probability')

        plt.show()
        
#Classe da Janela de visualização dos dados do banco de dados        
class Widget(Qt.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualização de Dados")
        
        layout = Qt.QVBoxLayout(self)

        btn_layout = Qt.QHBoxLayout()
        # !!!
        btn_layout.addItem(Qt.QSpacerItem(0, 0, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum))

#Botões funcionais da janela de visualização 

        btn1 = Qt.QPushButton("Análise SA1")
        btn1.clicked.connect(self.loadtable1)
        btn2 = Qt.QPushButton("Análise SA2")
        btn2.clicked.connect(self.loadtable2)
        btn3 = Qt.QPushButton("Análise SA3")
        btn3.clicked.connect(self.loadtable3)
        
        btn4 = Qt.QPushButton("Gráfico")
        btn4.clicked.connect(self.grafico)

        btn_layout.addWidget(btn1)
        btn_layout.addWidget(btn2)
        btn_layout.addWidget(btn3)
        btn_layout.addWidget(btn4)
        
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(16)

        self.tableWidget.setHorizontalHeaderLabels(('Número da Análise', 'Análise SA', 'Fornecedor', 'Fator1', 'Fator2', 'Fator3', 'Fator4', 'Fator5', 'Fator6', 'Fator7', 'Fator8', 'Fator9', 'Fator10', 'Fator11', 'Fator12', 'Parâmetro de Qualidade 1'))

        layout.addWidget(self.tableWidget)

        layout.addLayout(btn_layout)

#Função que recupera os dados do banco e exibe na janela
    
    def loadtable1(self):
        connection = sqlite3.connect('coletabeta.db')
        query = "SELECT * FROM Sa1"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()

    def loadtable2(self):
        connection = sqlite3.connect('coletabeta.db')
        query = "SELECT * FROM Sa2"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()
        
    def loadtable3(self):
        connection = sqlite3.connect('coletabeta.db')
        query = "SELECT * FROM Sa3"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()

#Função que chama a janela com os botões de geração dos gráficos

    def grafico(self):
        self.anotherwindow = imporSA()
        self.anotherwindow.show()
        
if __name__ == '__main__':
    app = Qt.QApplication([])
    w = Widget()
    w.show()
    app.exec()
