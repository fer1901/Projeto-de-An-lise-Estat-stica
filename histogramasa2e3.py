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

result = c.execute('SELECT Fator12 FROM Sa2')
data = np.array(c.fetchall())

        ## dados do banco
Fator12 = []

for i in range(15):
    Fator12.append(eval (data[i][0]))

print(Fator12)
        
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
plt.figtext(.70, .75, str(m), fontsize = 10)
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