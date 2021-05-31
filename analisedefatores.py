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
import statistics
import numpy as np
import pandas as pd
style.use('fivethirtyeight')

class adf1(Qt.QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'Análise real de fatores'
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.left = 0
        self.top = 0
        self.width = 200
        self.height = 200
   
        self.setWindowTitle(self.title) 
        self.setGeometry(self.left, self.top, self.width, self.height) 

        self.show() 

#Classe da janela de análise
class imporSA(Qt.QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Análise estatística de fatores'
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.left = 0
        self.top = 0
        self.width = 200
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

        self.tableWidget.setHorizontalHeaderLabels(('Gráfico da Análise', 'Histograma da Análise'))

#Botões dos Gráficos Normalizados

        btnFN1 = QPushButton(self.tableWidget)
        btnFN1.setText('Histograma do Fator 1')
        self.tableWidget.setCellWidget(0,1, btnFN1)
        btnFN1.clicked.connect(self.grafnormF1)

        btnFN2 = QPushButton(self.tableWidget)
        btnFN2.setText('Histograma do Fator 2')
        self.tableWidget.setCellWidget(1,1, btnFN2)
        btnFN2.clicked.connect(self.grafnormF2)

        btnFN3 = QPushButton(self.tableWidget)
        btnFN3.setText('Histograma do Fator 3')
        self.tableWidget.setCellWidget(2,1, btnFN3)
        btnFN3.clicked.connect(self.grafnormF3)

        btnFN4 = QPushButton(self.tableWidget)
        btnFN4.setText('Histograma do Fator 4')
        self.tableWidget.setCellWidget(3,1, btnFN4)
        btnFN4.clicked.connect(self.grafnormF4)

        btnFN5 = QPushButton(self.tableWidget)
        btnFN5.setText('Histograma do Fator 5')
        self.tableWidget.setCellWidget(4,1, btnFN5)
        btnFN5.clicked.connect(self.grafnormF5)

        btnFN6 = QPushButton(self.tableWidget)
        btnFN6.setText('Histograma do Fator 6')
        self.tableWidget.setCellWidget(5,1, btnFN6)
        btnFN6.clicked.connect(self.grafnormF6)

        btnFN7 = QPushButton(self.tableWidget)
        btnFN7.setText('Histograma do Fator 7')
        self.tableWidget.setCellWidget(6,1, btnFN7)
        btnFN7.clicked.connect(self.grafnormF7)

        btnFN8 = QPushButton(self.tableWidget)
        btnFN8.setText('Histograma do Fator 8')
        self.tableWidget.setCellWidget(7,1, btnFN8)
        btnFN8.clicked.connect(self.grafnormF8)

        btnFN9 = QPushButton(self.tableWidget)
        btnFN9.setText('Histograma do Fator 9')
        self.tableWidget.setCellWidget(8,1, btnFN9)
        btnFN9.clicked.connect(self.grafnormF9)

        btnFN10 = QPushButton(self.tableWidget)
        btnFN10.setText('Histograma do Fator 10')
        self.tableWidget.setCellWidget(9,1, btnFN10)
        btnFN10.clicked.connect(self.grafnormF10)

        btnFN11 = QPushButton(self.tableWidget)
        btnFN11.setText('Histograma do Fator 11')
        self.tableWidget.setCellWidget(10,1, btnFN11)
        btnFN11.clicked.connect(self.grafnormF11)

        btnFN12 = QPushButton(self.tableWidget)
        btnFN12.setText('Histograma do Fator 12')
        self.tableWidget.setCellWidget(11,1, btnFN12)
        btnFN12.clicked.connect(self.grafnormF12)

        btnFN13 = QPushButton(self.tableWidget)
        btnFN13.setText('Histograma do Fator 13')
        self.tableWidget.setCellWidget(12,1, btnFN13)
        btnFN13.clicked.connect(self.grafnormF13)

        btnFN14 = QPushButton(self.tableWidget)
        btnFN14.setText('Histograma do Fator 14')
        self.tableWidget.setCellWidget(13,1, btnFN14)
        btnFN14.clicked.connect(self.grafnormF14)

        btnFN15 = QPushButton(self.tableWidget)
        btnFN15.setText('Histograma do Fator 15')
        self.tableWidget.setCellWidget(14,1, btnFN15)
        btnFN15.clicked.connect(self.grafnormF15)

        btnFN16 = QPushButton(self.tableWidget)
        btnFN16.setText('Histograma do Fator 16')
        self.tableWidget.setCellWidget(15,1, btnFN16)
        btnFN16.clicked.connect(self.grafnormF16)

        btnFN17 = QPushButton(self.tableWidget)
        btnFN17.setText('Histograma do Fator 17')
        self.tableWidget.setCellWidget(16,1, btnFN17)
        btnFN17.clicked.connect(self.grafnormF17)

        btnFN18 = QPushButton(self.tableWidget)
        btnFN18.setText('Histograma do Fator 18')
        self.tableWidget.setCellWidget(17,1, btnFN18)
        btnFN18.clicked.connect(self.grafnormF18)

        btnFN19 = QPushButton(self.tableWidget)
        btnFN19.setText('Histograma do Fator 19')
        self.tableWidget.setCellWidget(18,1, btnFN19)
        btnFN19.clicked.connect(self.grafnormF19)

        btnFN20 = QPushButton(self.tableWidget)
        btnFN20.setText('Histograma do Fator 20')
        self.tableWidget.setCellWidget(19,1, btnFN20)
        btnFN20.clicked.connect(self.grafnormF20)

        btnFN21 = QPushButton(self.tableWidget)
        btnFN21.setText('Histograma do Fator 21')
        self.tableWidget.setCellWidget(20,1, btnFN21)
        btnFN21.clicked.connect(self.grafnormF21)

        btnFN22 = QPushButton(self.tableWidget)
        btnFN22.setText('Histograma do Fator 22')
        self.tableWidget.setCellWidget(21,1, btnFN22)
        btnFN22.clicked.connect(self.grafnormF22)

        btnFN23 = QPushButton(self.tableWidget)
        btnFN23.setText('Histograma do Fator 23')
        self.tableWidget.setCellWidget(22,1, btnFN23)
        btnFN23.clicked.connect(self.grafnormF23)

        btnFN24 = QPushButton(self.tableWidget)
        btnFN24.setText('Histograma do Fator 24')
        self.tableWidget.setCellWidget(23,1, btnFN24)
        btnFN24.clicked.connect(self.grafnormF24)

        btnFN25 = QPushButton(self.tableWidget)
        btnFN25.setText('Histograma do Fator 25')
        self.tableWidget.setCellWidget(24,1, btnFN25)
        btnFN25.clicked.connect(self.grafnormF25)

        btnFN26 = QPushButton(self.tableWidget)
        btnFN26.setText('Histograma do Fator 26')
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

        # Configuração de Visualização
        plt.plot(Id, Fator1, '-', color='Blue')  

        #Média
        m = statistics.mean(Fator1) 

        #variância
        v = statistics.pvariance(Fator1)

        #Desvio Padrão
        d = statistics.stdev(Fator1)

        #Mínimo 
        mi = statistics.median_low(Fator1)

        #Máximo
        ma = statistics.median_high(Fator1)

        #Erro Padrão
        er = np.std(Fator1, ddof=1) / np.sqrt(np.size(Fator1))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 1')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 1", 
                fontsize=20, 
                color="Black") 

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

                # Configuração de Visualização
        plt.plot(Id, Fator2, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator2) 

        #variância
        v = statistics.pvariance(Fator2)

        #Desvio Padrão
        d = statistics.stdev(Fator2)

        #Mínimo 
        mi = statistics.median_low(Fator2)

        #Máximo
        ma = statistics.median_high(Fator2)

        #Erro Padrão
        er = np.std(Fator2, ddof=1) / np.sqrt(np.size(Fator2))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 1')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 1", 
                fontsize=20, 
                color="Black")
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

                # Configuração de Visualização
        plt.plot(Id, Fator3, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator3) 

        #variância
        v = statistics.pvariance(Fator3)

        #Desvio Padrão
        d = statistics.stdev(Fator3)

        #Mínimo 
        mi = statistics.median_low(Fator3)

        #Máximo
        ma = statistics.median_high(Fator3)

        #Erro Padrão
        er = np.std(Fator3, ddof=1) / np.sqrt(np.size(Fator3))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 3')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 3", 
                fontsize=20, 
                color="Black")
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

                # Configuração de Visualização
        plt.plot(Id, Fator4, '-', color='Blue')  

        #Média
        m = statistics.mean(Fator4) 

        #variância
        v = statistics.pvariance(Fator4)

        #Desvio Padrão
        d = statistics.stdev(Fator4)

        #Mínimo 
        mi = statistics.median_low(Fator4)

        #Máximo
        ma = statistics.median_high(Fator4)

        #Erro Padrão
        er = np.std(Fator4, ddof=1) / np.sqrt(np.size(Fator4))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 4')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 4", 
                fontsize=20, 
                color="Black")

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

                # Configuração de Visualização
        plt.plot(Id, Fator5, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator5) 

        #variância
        v = statistics.pvariance(Fator5)

        #Desvio Padrão
        d = statistics.stdev(Fator5)

        #Mínimo 
        mi = statistics.median_low(Fator5)

        #Máximo
        ma = statistics.median_high(Fator5)

        #Erro Padrão
        er = np.std(Fator5, ddof=1) / np.sqrt(np.size(Fator5))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 5')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 5", 
                fontsize=20, 
                color="Black")

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

        # Configuração de Visualização
        plt.plot(Id, Fator6, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator6) 

        #variância
        v = statistics.pvariance(Fator6)

        #Desvio Padrão
        d = statistics.stdev(Fator6)

        #Mínimo 
        mi = statistics.median_low(Fator6)

        #Máximo
        ma = statistics.median_high(Fator6)

        #Erro Padrão
        er = np.std(Fator6, ddof=1) / np.sqrt(np.size(Fator6))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 6')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 6", 
                fontsize=20, 
                color="Black")

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

        # Configuração de Visualização
        plt.plot(Id, Fator7, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator7) 

        #variância
        v = statistics.pvariance(Fator7)

        #Desvio Padrão
        d = statistics.stdev(Fator7)

        #Mínimo 
        mi = statistics.median_low(Fator7)

        #Máximo
        ma = statistics.median_high(Fator7)

        #Erro Padrão
        er = np.std(Fator7, ddof=1) / np.sqrt(np.size(Fator7))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 7')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 7", 
                fontsize=20, 
                color="Black")
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

                # Configuração de Visualização
        plt.plot(Id, Fator8, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator8) 

        #variância
        v = statistics.pvariance(Fator8)

        #Desvio Padrão
        d = statistics.stdev(Fator8)

        #Mínimo 
        mi = statistics.median_low(Fator8)

        #Máximo
        ma = statistics.median_high(Fator8)

        #Erro Padrão
        er = np.std(Fator8, ddof=1) / np.sqrt(np.size(Fator8))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 8')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 8", 
                fontsize=20, 
                color="Black")
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

                # Configuração de Visualização
        plt.plot(Id, Fator9, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator9) 

        #variância
        v = statistics.pvariance(Fator9)

        #Desvio Padrão
        d = statistics.stdev(Fator9)

        #Mínimo 
        mi = statistics.median_low(Fator9)

        #Máximo
        ma = statistics.median_high(Fator9)

        #Erro Padrão
        er = np.std(Fator9, ddof=1) / np.sqrt(np.size(Fator9))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 9')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 9", 
                fontsize=20, 
                color="Black")

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

                # Configuração de Visualização
        plt.plot(Id, Fator10, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator10) 

        #variância
        v = statistics.pvariance(Fator10)

        #Desvio Padrão
        d = statistics.stdev(Fator10)

        #Mínimo 
        mi = statistics.median_low(Fator10)

        #Máximo
        ma = statistics.median_high(Fator10)

        #Erro Padrão
        er = np.std(Fator10, ddof=1) / np.sqrt(np.size(Fator10))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator", 
                fontsize=20, 
                color="Black")

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

        # Configuração de Visualização
        plt.plot(Id, Fator11, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator11) 

        #variância
        v = statistics.pvariance(Fator11)

        #Desvio Padrão
        d = statistics.stdev(Fator11)

        #Mínimo 
        mi = statistics.median_low(Fator11)

        #Máximo
        ma = statistics.median_high(Fator11)

        #Erro Padrão
        er = np.std(Fator11, ddof=1) / np.sqrt(np.size(Fator11))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 11')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 11", 
                fontsize=20, 
                color="Black")

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

        # Configuração de Visualização
        plt.plot(Id, Fator12, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator12) 

        #variância
        v = statistics.pvariance(Fator12)

        #Desvio Padrão
        d = statistics.stdev(Fator12)

        #Mínimo 
        mi = statistics.median_low(Fator12)

        #Máximo
        ma = statistics.median_high(Fator12)

        #Erro Padrão
        er = np.std(Fator12, ddof=1) / np.sqrt(np.size(Fator12))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 12')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 12", 
                fontsize=20, 
                color="Black")

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

        # Configuração de Visualização
        plt.plot(Id, Fator13, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator13) 

        #variância
        v = statistics.pvariance(Fator13)

        #Desvio Padrão
        d = statistics.stdev(Fator13)

        #Mínimo 
        mi = statistics.median_low(Fator13)

        #Máximo
        ma = statistics.median_high(Fator13)

        #Erro Padrão
        er = np.std(Fator13, ddof=1) / np.sqrt(np.size(Fator13))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 13')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 13", 
                fontsize=20, 
                color="Black")
                
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

                # Configuração de Visualização
        plt.plot(Id, Fator14, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator14) 

        #variância
        v = statistics.pvariance(Fator14)

        #Desvio Padrão
        d = statistics.stdev(Fator14)

        #Mínimo 
        mi = statistics.median_low(Fator14)

        #Máximo
        ma = statistics.median_high(Fator14)

        #Erro Padrão
        er = np.std(Fator14, ddof=1) / np.sqrt(np.size(Fator14))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 14')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 14", 
                fontsize=20, 
                color="Black")

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

        # Configuração de Visualização
        plt.plot(Id, Fator15, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator15) 

        #variância
        v = statistics.pvariance(Fator15)

        #Desvio Padrão
        d = statistics.stdev(Fator15)

        #Mínimo 
        mi = statistics.median_low(Fator15)

        #Máximo
        ma = statistics.median_high(Fator15)

        #Erro Padrão
        er = np.std(Fator15, ddof=1) / np.sqrt(np.size(Fator15))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 15')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 15", 
                fontsize=20, 
                color="Black")

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

        # Configuração de Visualização
        plt.plot(Id, Fator16, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator16) 

        #variância
        v = statistics.pvariance(Fator16)

        #Desvio Padrão
        d = statistics.stdev(Fator16)

        #Mínimo 
        mi = statistics.median_low(Fator16)

        #Máximo
        ma = statistics.median_high(Fator16)

        #Erro Padrão
        er = np.std(Fator16, ddof=1) / np.sqrt(np.size(Fator16))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 16')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 16", 
                fontsize=20, 
                color="Black")

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

                # Configuração de Visualização
        plt.plot(Id, Fator17, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator17) 

        #variância
        v = statistics.pvariance(Fator17)

        #Desvio Padrão
        d = statistics.stdev(Fator17)

        #Mínimo 
        mi = statistics.median_low(Fator17)

        #Máximo
        ma = statistics.median_high(Fator17)

        #Erro Padrão
        er = np.std(Fator17, ddof=1) / np.sqrt(np.size(Fator17))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 17')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 17", 
                fontsize=20, 
                color="Black")

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

                # Configuração de Visualização
        plt.plot(Id, Fator18, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator18) 

        #variância
        v = statistics.pvariance(Fator18)

        #Desvio Padrão
        d = statistics.stdev(Fator18)

        #Mínimo 
        mi = statistics.median_low(Fator18)

        #Máximo
        ma = statistics.median_high(Fator18)

        #Erro Padrão
        er = np.std(Fator18, ddof=1) / np.sqrt(np.size(Fator18))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 18')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 18", 
                fontsize=20, 
                color="Black")

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

        # Configuração de Visualização
        plt.plot(Id, Fator19, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator19) 

        #variância
        v = statistics.pvariance(Fator19)

        #Desvio Padrão
        d = statistics.stdev(Fator19)

        #Mínimo 
        mi = statistics.median_low(Fator19)

        #Máximo
        ma = statistics.median_high(Fator19)

        #Erro Padrão
        er = np.std(Fator19, ddof=1) / np.sqrt(np.size(Fator19))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 19')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 19", 
                fontsize=20, 
                color="Black")

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

        # Configuração de Visualização
        plt.plot(Id, Fator20, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator20) 

        #variância
        v = statistics.pvariance(Fator20)

        #Desvio Padrão
        d = statistics.stdev(Fator20)

        #Mínimo 
        mi = statistics.median_low(Fator20)

        #Máximo
        ma = statistics.median_high(Fator20)

        #Erro Padrão
        er = np.std(Fator20, ddof=1) / np.sqrt(np.size(Fator20))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 20')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 20", 
                fontsize=20, 
                color="Black")

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

                # Configuração de Visualização
        plt.plot(Id, Fator21, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator21) 

        #variância
        v = statistics.pvariance(Fator21)

        #Desvio Padrão
        d = statistics.stdev(Fator21)

        #Mínimo 
        mi = statistics.median_low(Fator21)

        #Máximo
        ma = statistics.median_high(Fator21)

        #Erro Padrão
        er = np.std(Fator21, ddof=1) / np.sqrt(np.size(Fator21))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 21')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 21", 
                fontsize=20, 
                color="Black")

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

                # Configuração de Visualização
        plt.plot(Id, Fator22, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator22) 

        #variância
        v = statistics.pvariance(Fator22)

        #Desvio Padrão
        d = statistics.stdev(Fator22)

        #Mínimo 
        mi = statistics.median_low(Fator22)

        #Máximo
        ma = statistics.median_high(Fator22)

        #Erro Padrão
        er = np.std(Fator22, ddof=1) / np.sqrt(np.size(Fator22))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 22')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 22", 
                fontsize=20, 
                color="Black")
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

                # Configuração de Visualização
        plt.plot(Id, Fator23, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator23) 

        #variância
        v = statistics.pvariance(Fator23)

        #Desvio Padrão
        d = statistics.stdev(Fator23)

        #Mínimo 
        mi = statistics.median_low(Fator23)

        #Máximo
        ma = statistics.median_high(Fator23)

        #Erro Padrão
        er = np.std(Fator23, ddof=1) / np.sqrt(np.size(Fator23))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 23')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 23", 
                fontsize=20, 
                color="Black")

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

                # Configuração de Visualização
        plt.plot(Id, Fator24, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator24) 

        #variância
        v = statistics.pvariance(Fator24)

        #Desvio Padrão
        d = statistics.stdev(Fator24)

        #Mínimo 
        mi = statistics.median_low(Fator24)

        #Máximo
        ma = statistics.median_high(Fator24)

        #Erro Padrão
        er = np.std(Fator24, ddof=1) / np.sqrt(np.size(Fator24))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 24')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 24", 
                fontsize=20, 
                color="Black")
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

                # Configuração de Visualização
        plt.plot(Id, Fator25, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator25) 

        #variância
        v = statistics.pvariance(Fator25)

        #Desvio Padrão
        d = statistics.stdev(Fator25)

        #Mínimo 
        mi = statistics.median_low(Fator25)

        #Máximo
        ma = statistics.median_high(Fator25)

        #Erro Padrão
        er = np.std(Fator25, ddof=1) / np.sqrt(np.size(Fator25))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 25')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 25", 
                fontsize=20, 
                color="Black")

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

                # Configuração de Visualização
        plt.plot(Id, Fator26, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator26) 

        #variância
        v = statistics.pvariance(Fator26)

        #Desvio Padrão
        d = statistics.stdev(Fator26)

        #Mínimo 
        mi = statistics.median_low(Fator26)

        #Máximo
        ma = statistics.median_high(Fator26)

        #Erro Padrão
        er = np.std(Fator26, ddof=1) / np.sqrt(np.size(Fator26))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 26')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 26", 
                fontsize=20, 
                color="Black")
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

                # Configuração de Visualização
        plt.plot(Id, Fator27, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator27) 

        #variância
        v = statistics.pvariance(Fator27)

        #Desvio Padrão
        d = statistics.stdev(Fator27)

        #Mínimo 
        mi = statistics.median_low(Fator27)

        #Máximo
        ma = statistics.median_high(Fator27)

        #Erro Padrão
        er = np.std(Fator27, ddof=1) / np.sqrt(np.size(Fator27))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 27')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 27", 
                fontsize=20, 
                color="Black")

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

                # Configuração de Visualização
        plt.plot(Id, Fator28, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator28) 

        #variância
        v = statistics.pvariance(Fator28)

        #Desvio Padrão
        d = statistics.stdev(Fator28)

        #Mínimo 
        mi = statistics.median_low(Fator28)

        #Máximo
        ma = statistics.median_high(Fator28)

        #Erro Padrão
        er = np.std(Fator28, ddof=1) / np.sqrt(np.size(Fator28))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 28')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 28", 
                fontsize=20, 
                color="Black")

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

                # Configuração de Visualização
        plt.plot(Id, Fator29, '-', color='Blue')  
        #Média
        m = statistics.mean(Fator29) 

        #variância
        v = statistics.pvariance(Fator29)

        #Desvio Padrão
        d = statistics.stdev(Fator29)

        #Mínimo 
        mi = statistics.median_low(Fator29)

        #Máximo
        ma = statistics.median_high(Fator29)

        #Erro Padrão
        er = np.std(Fator29, ddof=1) / np.sqrt(np.size(Fator29))


        plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.75, .75, " Média", fontsize = 10)
        plt.figtext(.87, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.75, .70, " Variância", fontsize = 10)
        plt.figtext(.87, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.87, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.75, .60, " Mínimo", fontsize = 10)
        plt.figtext(.87, .60, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.75, .55, " Máximo", fontsize = 10)
        plt.figtext(.87, .55, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
        plt.figtext(.87, .50, str("%.3f" % (er)), fontsize = 10)
        
    
        plt.xlabel('Numero de análises')  
  
        plt.ylabel('Fator 29')  
        
        # Configuração do título e cor do gráfico
        plt.title(label="Gráfico Nº de análises x Fator 29", 
                fontsize=20, 
                color="Black")

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

        Fator1 = []

        for row in data:
            Fator1.append(row[0])

        # Configuração de Visualização
        sns.histplot(Fator1,color='cyan')

        #Média
        m = statistics.mean(Fator1)

        #variância
        v = statistics.pvariance(Fator1)

        #Desvio Padrão
        d = statistics.stdev(Fator1)
            
        #Mediana
        med = statistics.median(Fator1)

        #Mínimo 
        mi = np.min(Fator1)

        #Máximo
        ma = np.max(Fator1)

        #Erro Padrão
        er = np.std(Fator1, ddof=1) / np.sqrt(np.size(Fator1))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF2(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator2 FROM Sa1')
        data = np.array(c.fetchall())

        Fator2 = []

        for row in data:
            Fator2.append(row[0])

        # Configuração de Visualização
        sns.histplot(Fator2,color='cyan')

        #Média
        m = statistics.mean(Fator2)

        #variância
        v = statistics.pvariance(Fator2)

        #Desvio Padrão
        d = statistics.stdev(Fator2)
            
        #Mediana
        med = statistics.median(Fator2)

        #Mínimo 
        mi = np.min(Fator2)

        #Máximo
        ma = np.max(Fator2)

        #Erro Padrão
        er = np.std(Fator2, ddof=1) / np.sqrt(np.size(Fator2))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF3(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator3 FROM Sa1')
        data = np.array(c.fetchall())

        Fator3 = []

        for row in data:
            Fator3.append(row[0])

        # Configuração de Visualização
        sns.histplot(Fator3,color='cyan')

        #Média
        m = statistics.mean(Fator3)

        #variância
        v = statistics.pvariance(Fator3)

        #Desvio Padrão
        d = statistics.stdev(Fator3)
            
        #Mediana
        med = statistics.median(Fator3)

        #Mínimo 
        mi = np.min(Fator3)

        #Máximo
        ma = np.max(Fator3)

        #Erro Padrão
        er = np.std(Fator3, ddof=1) / np.sqrt(np.size(Fator3))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF4(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator4 FROM Sa1')
        data = np.array(c.fetchall())

        Fator4 = []

        for row in data:
            Fator4.append(row[0])

        # Configuração de Visualização
        sns.histplot(Fator4,color='cyan')

        #Média
        m = statistics.mean(Fator4)

        #variância
        v = statistics.pvariance(Fator4)

        #Desvio Padrão
        d = statistics.stdev(Fator4)
            
        #Mediana
        med = statistics.median(Fator4)

        #Mínimo 
        mi = np.min(Fator4)

        #Máximo
        ma = np.max(Fator4)

        #Erro Padrão
        er = np.std(Fator4, ddof=1) / np.sqrt(np.size(Fator4))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF5(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator5 FROM Sa1')
        data = np.array(c.fetchall())

        Fator5 = []

        for row in data:
            Fator5.append(row[0])

        # Configuração de Visualização
        sns.histplot(Fator5,color='cyan')

        #Média
        m = statistics.mean(Fator5)

        #variância
        v = statistics.pvariance(Fator5)

        #Desvio Padrão
        d = statistics.stdev(Fator5)
            
        #Mediana
        med = statistics.median(Fator5)

        #Mínimo 
        mi = np.min(Fator5)

        #Máximo
        ma = np.max(Fator5)

        #Erro Padrão
        er = np.std(Fator5, ddof=1) / np.sqrt(np.size(Fator5))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF6(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator6 FROM Sa1')
        data = np.array(c.fetchall())

        Fator6 = []

        for row in data:
            Fator6.append(row[0])

        # Configuração de Visualização
        sns.histplot(Fator6,color='cyan')

        #Média
        m = statistics.mean(Fator6)

        #variância
        v = statistics.pvariance(Fator6)

        #Desvio Padrão
        d = statistics.stdev(Fator6)
            
        #Mediana
        med = statistics.median(Fator6)

        #Mínimo 
        mi = np.min(Fator6)

        #Máximo
        ma = np.max(Fator6)

        #Erro Padrão
        er = np.std(Fator6, ddof=1) / np.sqrt(np.size(Fator6))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF7(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator7 FROM Sa1')
        data = np.array(c.fetchall())

        Fator7 = []

        for row in data:
            Fator7.append(row[0])

        # Configuração de Visualização
        sns.histplot(Fator7,color='cyan')

        #Média
        m = statistics.mean(Fator7)

        #variância
        v = statistics.pvariance(Fator7)

        #Desvio Padrão
        d = statistics.stdev(Fator7)
            
        #Mediana
        med = statistics.median(Fator7)

        #Mínimo 
        mi = np.min(Fator7)

        #Máximo
        ma = np.max(Fator7)

        #Erro Padrão
        er = np.std(Fator7, ddof=1) / np.sqrt(np.size(Fator7))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF8(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator8 FROM Sa1')
        data = np.array(c.fetchall())

        Fator8 = []

        for row in data:
            Fator8.append(row[0])

        # Configuração de Visualização
        sns.histplot(Fator8,color='cyan')

        #Média
        m = statistics.mean(Fator8)

        #variância
        v = statistics.pvariance(Fator8)

        #Desvio Padrão
        d = statistics.stdev(Fator8)
            
        #Mediana
        med = statistics.median(Fator8)

        #Mínimo 
        mi = np.min(Fator8)

        #Máximo
        ma = np.max(Fator8)

        #Erro Padrão
        er = np.std(Fator8, ddof=1) / np.sqrt(np.size(Fator8))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF9(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator9 FROM Sa1')
        data = np.array(c.fetchall())

        Fator9 = []

        for row in data:
            Fator9.append(row[0])

        # Configuração de Visualização
        sns.histplot(Fator9,color='cyan')

        #Média
        m = statistics.mean(Fator9)

        #variância
        v = statistics.pvariance(Fator9)

        #Desvio Padrão
        d = statistics.stdev(Fator9)
            
        #Mediana
        med = statistics.median(Fator9)

        #Mínimo 
        mi = np.min(Fator9)

        #Máximo
        ma = np.max(Fator9)

        #Erro Padrão
        er = np.std(Fator9, ddof=1) / np.sqrt(np.size(Fator9))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF10(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator10 FROM Sa1')
        data = np.array(c.fetchall())

        Fator10 = []

        for row in data:
            Fator10.append(row[0])

        # Configuração de Visualização
        sns.histplot(Fator10,color='cyan')

        #Média
        m = statistics.mean(Fator10)

        #variância
        v = statistics.pvariance(Fator10)

        #Desvio Padrão
        d = statistics.stdev(Fator10)
            
        #Mediana
        med = statistics.median(Fator10)

        #Mínimo 
        mi = np.min(Fator10)

        #Máximo
        ma = np.max(Fator10)

        #Erro Padrão
        er = np.std(Fator10, ddof=1) / np.sqrt(np.size(Fator10))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF11(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator11 FROM Sa1')
        data = np.array(c.fetchall())

        Fator11 = []

        for row in data:
            Fator11.append(row[0])

        # Configuração de Visualização
        sns.histplot(Fator11,color='cyan')

        #Média
        m = statistics.mean(Fator11)

        #variância
        v = statistics.pvariance(Fator11)

        #Desvio Padrão
        d = statistics.stdev(Fator11)
            
        #Mediana
        med = statistics.median(Fator11)

        #Mínimo 
        mi = np.min(Fator11)

        #Máximo
        ma = np.max(Fator11)

        #Erro Padrão
        er = np.std(Fator11, ddof=1) / np.sqrt(np.size(Fator11))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF12(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator12 FROM Sa2')
        data = np.array(c.fetchall())

                ## dados do banco
        Fator12 = []

        for i in range(15):
            Fator12.append(eval (data[i][0]))
                
        #Fator12 = np.array(Fator12)

                        
        # Configuração de Visualização
        sns.histplot(Fator12,color='cyan')

        #Média
        m = statistics.mean(Fator12)

        #variância
        v = statistics.pvariance(Fator12)

        #Desvio Padrão
        d = statistics.stdev(Fator12)
            
        #Mediana
        med = statistics.median(Fator12)

        #Mínimo 
        mi = np.min(Fator12)

        #Máximo
        ma = np.max(Fator12)

        #Erro Padrão
        er = np.std(Fator12, ddof=1) / np.sqrt(np.size(Fator12))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF13(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator12 FROM Sa2')
        data = np.array(c.fetchall())

                ## dados do banco
        Fator13 = []

        for i in range(15):
            Fator13.append(eval (data[i][0]))

                        
        # Configuração de Visualização
        sns.histplot(Fator13,color='cyan')

        #Média
        m = statistics.mean(Fator13)

        #variância
        v = statistics.pvariance(Fator13)

        #Desvio Padrão
        d = statistics.stdev(Fator13)
            
        #Mediana
        med = statistics.median(Fator13)

        #Mínimo 
        mi = np.min(Fator13)

        #Máximo
        ma = np.max(Fator13)

        #Erro Padrão
        er = np.std(Fator13, ddof=1) / np.sqrt(np.size(Fator13))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF14(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator14 FROM Sa2')
        data = np.array(c.fetchall())

        ## dados do banco
        Fator14 = []

        for i in range(15):
            Fator14.append(eval (data[i][0]))

                        
        # Configuração de Visualização
        sns.histplot(Fator14,color='cyan')

        #Média
        m = statistics.mean(Fator14)

        #variância
        v = statistics.pvariance(Fator14)

        #Desvio Padrão
        d = statistics.stdev(Fator14)
            
        #Mediana
        med = statistics.median(Fator14)

        #Mínimo 
        mi = np.min(Fator14)

        #Máximo
        ma = np.max(Fator14)

        #Erro Padrão
        er = np.std(Fator14, ddof=1) / np.sqrt(np.size(Fator14))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF15(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator15 FROM Sa2')
        data = np.array(c.fetchall())

        ## dados do banco
        Fator15 = []

        for i in range(15):
            Fator15.append(eval (data[i][0]))

                        
        # Configuração de Visualização
        sns.histplot(Fator15,color='cyan')

        #Média
        m = statistics.mean(Fator15)

        #variância
        v = statistics.pvariance(Fator15)

        #Desvio Padrão
        d = statistics.stdev(Fator15)
            
        #Mediana
        med = statistics.median(Fator15)

        #Mínimo 
        mi = np.min(Fator15)

        #Máximo
        ma = np.max(Fator15)

        #Erro Padrão
        er = np.std(Fator15, ddof=1) / np.sqrt(np.size(Fator15))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF16(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator16 FROM Sa2')
        data = np.array(c.fetchall())

        Fator16 = []

        for i in range(15):
            Fator16.append(eval (data[i][0]))

                        
        # Configuração de Visualização
        sns.histplot(Fator16,color='cyan')

        #Média
        m = statistics.mean(Fator16)

        #variância
        v = statistics.pvariance(Fator16)

        #Desvio Padrão
        d = statistics.stdev(Fator16)
            
        #Mediana
        med = statistics.median(Fator16)

        #Mínimo 
        mi = np.min(Fator16)

        #Máximo
        ma = np.max(Fator16)

        #Erro Padrão
        er = np.std(Fator16, ddof=1) / np.sqrt(np.size(Fator16))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF17(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator17 FROM Sa2')
        data = np.array(c.fetchall())

        ## dados do banco
        Fator17 = []

        for i in range(15):
            Fator17.append(eval (data[i][0]))

                        
        # Configuração de Visualização
        sns.histplot(Fator17,color='cyan')

        #Média
        m = statistics.mean(Fator17)

        #variância
        v = statistics.pvariance(Fator17)

        #Desvio Padrão
        d = statistics.stdev(Fator17)
            
        #Mediana
        med = statistics.median(Fator17)

        #Mínimo 
        mi = np.min(Fator17)

        #Máximo
        ma = np.max(Fator17)

        #Erro Padrão
        er = np.std(Fator17, ddof=1) / np.sqrt(np.size(Fator17))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF18(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator18 FROM Sa2')
        data = np.array(c.fetchall())
        Fator18 = []

        for i in range(15):
            Fator18.append(eval (data[i][0]))

                        
        # Configuração de Visualização
        sns.histplot(Fator18,color='cyan')

        #Média
        m = statistics.mean(Fator18)

        #variância
        v = statistics.pvariance(Fator18)

        #Desvio Padrão
        d = statistics.stdev(Fator18)
            
        #Mediana
        med = statistics.median(Fator18)

        #Mínimo 
        mi = np.min(Fator18)

        #Máximo
        ma = np.max(Fator18)

        #Erro Padrão
        er = np.std(Fator18, ddof=1) / np.sqrt(np.size(Fator18))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF19(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator19 FROM Sa2')
        data = np.array(c.fetchall())

        ## dados do banco
        Fator19 = []

        for i in range(15):
            Fator19.append(eval (data[i][0]))

                        
        # Configuração de Visualização
        sns.histplot(Fator19,color='cyan')

        #Média
        m = statistics.mean(Fator19)

        #variância
        v = statistics.pvariance(Fator19)

        #Desvio Padrão
        d = statistics.stdev(Fator19)
            
        #Mediana
        med = statistics.median(Fator19)

        #Mínimo 
        mi = np.min(Fator19)

        #Máximo
        ma = np.max(Fator19)

        #Erro Padrão
        er = np.std(Fator19, ddof=1) / np.sqrt(np.size(Fator19))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF20(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator20 FROM Sa2')
        data = np.array(c.fetchall())

        Fator20 = []

        for i in range(15):
            Fator20.append(eval (data[i][0]))

                        
        # Configuração de Visualização
        sns.histplot(Fator20,color='cyan')

        #Média
        m = statistics.mean(Fator20)

        #variância
        v = statistics.pvariance(Fator20)

        #Desvio Padrão
        d = statistics.stdev(Fator20)
            
        #Mediana
        med = statistics.median(Fator20)

        #Mínimo 
        mi = np.min(Fator20)

        #Máximo
        ma = np.max(Fator20)

        #Erro Padrão
        er = np.std(Fator20, ddof=1) / np.sqrt(np.size(Fator20))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF21(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator21 FROM Sa2')
        data = np.array(c.fetchall())

        ## dados do banco
        Fator21 = []

        for i in range(15):
            Fator21.append(eval (data[i][0]))

                        
        # Configuração de Visualização
        sns.histplot(Fator21,color='cyan')

        #Média
        m = statistics.mean(Fator21)

        #variância
        v = statistics.pvariance(Fator21)

        #Desvio Padrão
        d = statistics.stdev(Fator21)
            
        #Mediana
        med = statistics.median(Fator21)

        #Mínimo 
        mi = np.min(Fator21)

        #Máximo
        ma = np.max(Fator21)

        #Erro Padrão
        er = np.std(Fator21, ddof=1) / np.sqrt(np.size(Fator21))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()
    
    def grafnormF22(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator22 FROM Sa2')
        data = np.array(c.fetchall())

        Fator22 = []

        for i in range(15):
            Fator22.append(eval (data[i][0]))

                        
        # Configuração de Visualização
        sns.histplot(Fator22,color='cyan')

        #Média
        m = statistics.mean(Fator22)

        #variância
        v = statistics.pvariance(Fator22)

        #Desvio Padrão
        d = statistics.stdev(Fator22)
            
        #Mediana
        med = statistics.median(Fator22)

        #Mínimo 
        mi = np.min(Fator22)

        #Máximo
        ma = np.max(Fator22)

        #Erro Padrão
        er = np.std(Fator22, ddof=1) / np.sqrt(np.size(Fator22))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF23(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator23 FROM Sa3')
        data = np.array(c.fetchall())

        ## dados do banco
        Fator23 = []

        for i in range(15):
            Fator23.append(eval (data[i][0]))

                        
        # Configuração de Visualização
        sns.histplot(Fator23,color='cyan')

        #Média
        m = statistics.mean(Fator23)

        #variância
        v = statistics.pvariance(Fator23)

        #Desvio Padrão
        d = statistics.stdev(Fator23)
            
        #Mediana
        med = statistics.median(Fator23)

        #Mínimo 
        mi = np.min(Fator23)

        #Máximo
        ma = np.max(Fator23)

        #Erro Padrão
        er = np.std(Fator23, ddof=1) / np.sqrt(np.size(Fator23))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF24(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator24 FROM Sa3')
        data = np.array(c.fetchall())

        

        ## dados do banco
        Fator24 = []

        for i in range(15):
            Fator24.append(eval (data[i][0]))

                        
        # Configuração de Visualização
        sns.histplot(Fator24,color='cyan')

        #Média
        m = statistics.mean(Fator24)

        #variância
        v = statistics.pvariance(Fator24)

        #Desvio Padrão
        d = statistics.stdev(Fator24)
            
        #Mediana
        med = statistics.median(Fator24)

        #Mínimo 
        mi = np.min(Fator24)

        #Máximo
        ma = np.max(Fator24)

        #Erro Padrão
        er = np.std(Fator24, ddof=1) / np.sqrt(np.size(Fator24))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF25(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator25 FROM Sa3')
        data = np.array(c.fetchall())

        ## dados do banco
        Fator25 = []

        for i in range(15):
            Fator25.append(eval (data[i][0]))

                        
        # Configuração de Visualização
        sns.histplot(Fator25,color='cyan')

        #Média
        m = statistics.mean(Fator25)

        #variância
        v = statistics.pvariance(Fator25)

        #Desvio Padrão
        d = statistics.stdev(Fator25)
            
        #Mediana
        med = statistics.median(Fator25)

        #Mínimo 
        mi = np.min(Fator25)

        #Máximo
        ma = np.max(Fator25)

        #Erro Padrão
        er = np.std(Fator25, ddof=1) / np.sqrt(np.size(Fator25))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF26(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator26 FROM Sa3')
        data = np.array(c.fetchall())

        

        ## dados do banco
        Fator26 = []

        for i in range(15):
            Fator26.append(eval (data[i][0]))

                        
        # Configuração de Visualização
        sns.histplot(Fator26,color='cyan')

        #Média
        m = statistics.mean(Fator26)

        #variância
        v = statistics.pvariance(Fator26)

        #Desvio Padrão
        d = statistics.stdev(Fator26)
            
        #Mediana
        med = statistics.median(Fator26)

        #Mínimo 
        mi = np.min(Fator26)

        #Máximo
        ma = np.max(Fator26)

        #Erro Padrão
        er = np.std(Fator26, ddof=1) / np.sqrt(np.size(Fator26))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF27(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator27 FROM Sa3')
        data = np.array(c.fetchall())

        ## dados do banco
        Fator27 = []

        for i in range(15):
            Fator27.append(eval (data[i][0]))

                        
        # Configuração de Visualização
        sns.histplot(Fator27,color='cyan')

        #Média
        m = statistics.mean(Fator27)

        #variância
        v = statistics.pvariance(Fator27)

        #Desvio Padrão
        d = statistics.stdev(Fator27)
            
        #Mediana
        med = statistics.median(Fator27)

        #Mínimo 
        mi = np.min(Fator27)

        #Máximo
        ma = np.max(Fator27)

        #Erro Padrão
        er = np.std(Fator27, ddof=1) / np.sqrt(np.size(Fator27))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF28(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator28 FROM Sa3')
        data = np.array(c.fetchall())

        ## dados do banco
        Fator28 = []

        for i in range(15):
            Fator28.append(eval (data[i][0]))

                        
        # Configuração de Visualização
        sns.histplot(Fator28,color='cyan')

        #Média
        m = statistics.mean(Fator28)

        #variância
        v = statistics.pvariance(Fator28)

        #Desvio Padrão
        d = statistics.stdev(Fator28)
            
        #Mediana
        med = statistics.median(Fator28)

        #Mínimo 
        mi = np.min(Fator28)

        #Máximo
        ma = np.max(Fator28)

        #Erro Padrão
        er = np.std(Fator28, ddof=1) / np.sqrt(np.size(Fator28))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()

    def grafnormF29(self): 
        # Conexão ao Banco de Dados Local
        conn = sqlite3.connect('coletabeta.db')
        c = conn.cursor()

        result = c.execute('SELECT Fator29 FROM Sa3')
        data = np.array(c.fetchall())

        Fator29 = []

        for i in range(15):
            Fator29.append(eval (data[i][0]))

                        
        # Configuração de Visualização
        sns.histplot(Fator29,color='cyan')

        #Média
        m = statistics.mean(Fator29)

        #variância
        v = statistics.pvariance(Fator29)

        #Desvio Padrão
        d = statistics.stdev(Fator29)
            
        #Mediana
        med = statistics.median(Fator29)

        #Mínimo 
        mi = np.min(Fator29)

        #Máximo
        ma = np.max(Fator29)

        #Erro Padrão
        er = np.std(Fator29, ddof=1) / np.sqrt(np.size(Fator29))
            
        plt.figtext(.60, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
        plt.figtext(.65, .75, " Média", fontsize = 10)
        plt.figtext(.70, .75, str("%.3f" % (m)), fontsize = 10)
        plt.figtext(.65, .70, " Variância", fontsize = 10)
        plt.figtext(.73, .70, str("%.3f" % (v)), fontsize = 10)
        plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
        plt.figtext(.74, .65, str("%.3f" % (d)), fontsize = 10)
        plt.figtext(.65, .60, " Mediana", fontsize = 10)
        plt.figtext(.73, .60, str("%.3f" % (med)), fontsize = 10)
        plt.figtext(.65, .55, " Mínimo", fontsize = 10)
        plt.figtext(.73, .55, str("%.3f" % (mi)), fontsize = 10)
        plt.figtext(.65, .50, " Máximo", fontsize = 10)
        plt.figtext(.73, .50, str("%.3f" % (ma)), fontsize = 10)
        plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
        plt.figtext(.73, .45, str("%.3f" % (er)), fontsize = 10)

        plt.xlabel('Fator')  
        plt.ylabel('Frequência')  
                
        # Configuração do título e cor do gráfico
        plt.title(label="Histograma", 
                    fontsize=30, 
                    color="Black") 

        plt.show()
        
#Classe da Janela de visualização dos dados do banco de dados        
class Widget(Qt.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualização de Dados")
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        
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

        btn5 = Qt.QPushButton("Análise dos Fatores")
        btn5.clicked.connect(self.adf)

        btn_layout.addWidget(btn1)
        btn_layout.addWidget(btn2)
        btn_layout.addWidget(btn3)
        btn_layout.addWidget(btn4)
        btn_layout.addWidget(btn5)
        
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(15)

        layout.addWidget(self.tableWidget)

        layout.addLayout(btn_layout)

#Função que recupera os dados do banco e exibe na janela
    
    def loadtable1(self):
        connection = sqlite3.connect('coletabeta.db')
        query = "SELECT * FROM Sa1"
        result = connection.execute(query)

        self.tableWidget.setHorizontalHeaderLabels(('Número da Análise', 'Análise SA', 'Fornecedor', 'Fator1', 'Fator2', 'Fator3', 'Fator4', 'Fator5', 'Fator6', 'Fator7', 'Fator8', 'Fator9', 'Fator10', 'Fator11', 'Parâmetro de Qualidade 1'))

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

        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(16)

        self.tableWidget.setHorizontalHeaderLabels(('Número da Análise', 'Análise SA1', 'Fator12', 'Fator13', 'Fator14', 'Fator15', 'Fator16', 'Fator17', 'Fator18', 'Fator19', 'Fator20', 'Fator21', 'Fator22', 'Parâmetro de Qualidade 2', 'Parâmetro de Qualidade3', 'Data da análise'))

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

        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(13)

        self.tableWidget.setHorizontalHeaderLabels(('Número da Análise', 'Análise SA2', 'Fator23', 'Fator24', 'Fator25', 'Fator26', 'Fator27', 'Fator28', 'Fator29', 'Parâmetro de Qualidade 4', 'Parâmetro de Qualidade 5', 'Parâmetro de Qualidade 6', 'Data da análise'))

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
        
#Função que chama a janela com os botões de geração dos gráficos

    def adf(self):
        self.anotherwindow = adf1()
        self.anotherwindow.show()

if __name__ == '__main__':
    app = Qt.QApplication([])
    w = Widget()
    w.show()
    app.exec()
