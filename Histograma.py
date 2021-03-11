# Import library and dataset
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
import statistics
style.use('fivethirtyeight')
        
# Conexão ao Banco de Dados Local
conn = sqlite3.connect('coletabeta.db')
c = conn.cursor()

result = c.execute('SELECT Fator2 FROM Sa1')
data = c.fetchall()

## dados do banco
Fator2 = [data]
for row in result:
    Fator2.append(float(row[1]))

# Configuração de Visualização
sns.histplot(data,color='black')

print(Fator2)

#Média
m = statistics.mean(Fator2) 


plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
plt.figtext(.75, .75, " Média", fontsize = 10)


plt.xlabel('Fator')  
plt.ylabel('Frequência')  
        
# Configuração do título e cor do gráfico
plt.title(label="Histograma", 
            fontsize=30, 
            color="Black") 

plt.show()