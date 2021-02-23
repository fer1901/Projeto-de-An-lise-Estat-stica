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

# Connect to database
conn = sqlite3.connect('coletabeta.db')
c = conn.cursor()

result = c.execute('SELECT Fator13 FROM Sa2')
data = np.array(c.fetchall())

print(type(data[0][0]))


## dados do banco

x = []
for i in range(15):
   x.append(eval (data[i][0]))
   
x = np.array(x)
   
sns.histplot(x,kde=True,stat='probability')

# Configuração de Visualização
sns.histplot(x,kde=True,stat='probability',color='Black')
plt.xlabel('Numero aleatório')  
plt.ylabel('Fator')  
        
# Configuração do título e cor do gráfico
plt.title(label="Gráfico Normalizado", 
            fontsize=30, 
            color="Black") 

plt.show()
