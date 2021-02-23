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

    #df = pd.read_sql_query("SELECT Id, Fator2 FROM Sa1", conn)
    #df = pd.Series

    for row in data:
        Id.append(row[0])
        Fator2.append(row[1])

#desvio padrão 
    #statistics.pstdev(df.head())
    #print(statistics.pstdev(df.head()))

#erro padrão 

#variância
    #statistics.pvariance(data)
    #print(statistics.pvariance(data))

#Minímo

    # depicting the visualization 

    plt.plot(Id, Fator2, '-', color='Blue') 
    
    plt.figtext(0, 0, "Dados Estatísticos", fontsize = 10) 
   
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