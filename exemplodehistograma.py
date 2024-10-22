#!/usr/bin/env python

import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
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

# example data
# Conexão ao Banco de Dados Local
conn = sqlite3.connect('coletabeta.db')
c = conn.cursor()

result = c.execute('SELECT Fator2 FROM Sa1')
data = np.array(c.fetchall())

## dados do banco
Fator2 = [data]
for row in result:
    Fator2.append(float(row[1]))


num_bins = 20
# the histogram of the data
n, bins, patches = plt.hist(data, num_bins, density=1, facecolor='blue', alpha=0.5)

# add a 'best fit' line
#y = mlab.normpdf(bins)
plt.plot(bins, 'r--')
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()
