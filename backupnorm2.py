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

# Connect to database
conn = sqlite3.connect('coletabeta.db')
c = conn.cursor()

result = c.execute('SELECT Id, Fator1 FROM Sa1')
data = c.fetchall()

## dados do banco
Fator1 = []
for row in result:
   Fator1.append(float(row[1]))


# configurando dados para plotar o gráfico
x = Fator1
num_bins = 500

# plotagem do gráfico
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.show()
conn.close()
