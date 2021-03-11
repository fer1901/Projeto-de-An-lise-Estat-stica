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
import statistics
import numpy as np
import pandas as pd

# Connect to database
conn = sqlite3.connect('coletabeta.db')
c = conn.cursor()

result = c.execute('SELECT Fator1 FROM Sa1')
data = c.fetchall()

## dados do banco
Fator1 = [data]
for row in result:
   Fator1.append(float(row[0]))

value = np.random.random_sample(size = 15)

mu = data
sigma = value

x = mu + sigma * np.random.randn(15)

hist, bins = np.histogram(x, bins=50, density=1)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)

print(Fator1)

#Média
#data1 = data
#m = statistics.mean(data1) 
#print(m)


plt.figtext(.74, .8, "Dados Estatísticos", color="Gray", fontsize = 14)
plt.figtext(.75, .75, " Média", fontsize = 10)

plt.xlabel('Fator')
plt.ylabel('Probability')
plt.title(r'Histograma')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()
