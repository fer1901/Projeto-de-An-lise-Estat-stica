from scipy.stats import norm
import seaborn as sns
 #for inline plots in jupyter
#%matplotlib inline
# import matplotlib
import matplotlib.pyplot as plt
# for latex equations
#from IPython.display import Math, Latex
# for displaying images
#from IPython.core.display import Image
# generate random numbers from N(0,1)
import seaborn
data_normal = norm.rvs(size=10000,loc=0,scale=1)
ax = sns.histplot(data_normal,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')