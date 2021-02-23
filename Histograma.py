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
        
# Conexão ao Banco de Dados Local
conn = sqlite3.connect('coletabeta.db')
c = conn.cursor()

result = c.execute('SELECT Fator2 FROM Sa1')
data = np.array(c.fetchall())

## dados do banco
Fator2 = []
for row in result:
    Fator2.append(float(row[1]))

# Configuração de Visualização
sns.histplot(data,color='black')
plt.xlabel('Numero aleatório')  
plt.ylabel('Fator')  
        
# Configuração do título e cor do gráfico
plt.title(label="Gráfico Normalizado", 
            fontsize=30, 
            color="Black") 

plt.show()