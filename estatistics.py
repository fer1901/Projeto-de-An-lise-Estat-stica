import sqlite3
import matplotlib
from matplotlib import style
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
from matplotlib.widgets import Button
import statistics
import numpy as np
import pandas as pd
style.use('fivethirtyeight')


def graph_data():
    # Connect to database
    conn = sqlite3.connect('coletabeta.db')
    c = conn.cursor()

    c.execute('SELECT Id, Fator2 FROM Sa1')
    data = np.array(c.fetchall())

    Id = []
    Fator2 = []

    for row in data:
        Id.append(row[0])
        Fator2.append(row[1])

    # depicting the visualization 

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
    plt.figtext(.87, .75, str(m), fontsize = 10)
    plt.figtext(.75, .70, " Variância", fontsize = 10)
    plt.figtext(.87, .70, str(v), fontsize = 10)
    plt.figtext(.75, .65, " Desvio Padrão", fontsize = 10)
    plt.figtext(.87, .65, str(d), fontsize = 10)
    plt.figtext(.75, .60, " Mínimo", fontsize = 10)
    plt.figtext(.87, .60, str(mi), fontsize = 10)
    plt.figtext(.75, .55, " Máximo", fontsize = 10)
    plt.figtext(.87, .55, str(ma), fontsize = 10)
    plt.figtext(.75, .50, " Erro Padrão", fontsize = 10)
    plt.figtext(.87, .50, str(er), fontsize = 10)
     
   
    plt.xlabel('Numero de análises')  
    plt.ylabel('Fator')  
    
    # displaying the title 
    plt.title(label="Gráfico Nº de análises x Fator", 
            fontsize=20, 
            color="Black") 

    plt.show()

    c.close()
    conn.close()

graph_data()