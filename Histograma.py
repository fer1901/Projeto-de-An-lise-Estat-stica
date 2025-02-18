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
import numpy as np  
        
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
plt.figtext(.73, .70, str(v), fontsize = 10)
plt.figtext(.65, .65, " Desvio Padrão", fontsize = 10)
plt.figtext(.74, .65, str(d), fontsize = 10)
plt.figtext(.65, .60, " Mediana", fontsize = 10)
plt.figtext(.73, .60, str(med), fontsize = 10)
plt.figtext(.65, .55, " Mínimo", fontsize = 10)
plt.figtext(.73, .55, str(mi), fontsize = 10)
plt.figtext(.65, .50, " Máximo", fontsize = 10)
plt.figtext(.73, .50, str(ma), fontsize = 10)
plt.figtext(.65, .45, " Erro Padrão", fontsize = 10)
plt.figtext(.73, .45, str(er), fontsize = 10)

plt.xlabel('Fator')  
plt.ylabel('Frequência')  
        
# Configuração do título e cor do gráfico
plt.title(label="Histograma", 
            fontsize=30, 
            color="Black") 

plt.show()