#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc


rc('text', usetex=True)

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True

df = pd.read_excel('./cardio/cardio.xlsx')

x=[]
y=[]


# Grup PG
for i in range(df.iloc[:,0].count()):
	y.append(df.iloc[i, 1])
	y.append(df.iloc[i,2])


x = list(2*np.arange(len(y)/2))
x = sorted(x*2)

print('x=',x)

fig, ax = plt.subplots(figsize=(12, 5), dpi=100)


#ax.annotate("", xy=(), xycoords='data', xytext = (x2, y2), textcoords='data',)
	#arrowprops=dict(arrowstyle="->",
		#connectionstyle="arc3"),


for i in range(len(x)//2 - 1):
	print('(',x[i*2],',',y[i*2],') to (',x[i*2+1],',',y[i*2+1],')')
	ax.plot(x[i*2:i*2+2], y[i*2:i*2+2], 'o', color='tab:orange')

	an1 = ax.annotate("%d" % y[i*2], xytext=(x[i*2], y[i*2]), xycoords='data', va="bottom", ha="center", xy = (x[i*2+1], y[i*2+1]), textcoords='data', arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

	ax.annotate("%d" % y[i*2+1], xytext=(0,-15), xycoords='data', va="baseline", ha="center", xy=(x[i*2+1], y[i*2+1]), textcoords='offset points')


ax.plot(x[i*2:i*2+2], y[i*2:i*2+2], 'o', color='tab:orange', label='Grup PG')
# GGrup IE
y=[]

for i in range(df.iloc[:,0].count()):
	y.append(df.iloc[i, 3])
	y.append(df.iloc[i,4])

x=[]

x = list(2*np.arange(len(y)/2)+1)
x = sorted(x*2)

print('x=',x)

for i in range(len(x)//2 - 1):
	ax.plot(x[i*2:i*2+2], y[i*2:i*2+2], 's', color='tab:purple')

	an1 = ax.annotate("%d" % y[i*2], xytext=(x[i*2], y[i*2]), xycoords='data', va="bottom", ha="center", xy = (x[i*2+1], y[i*2+1]), textcoords='data', arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

	ax.annotate("%d" % y[i*2+1], xytext=(0,-15), xycoords='data', va="baseline", ha="center", xy=(x[i*2+1], y[i*2+1]), textcoords='offset points')
	#ax.plot(x[i*2:i*2+2], y[i*2:i*2+2], mymark)

ax.plot(x[i*2:i*2+2], y[i*2:i*2+2], 's', color='tab:purple', label='Grup IE')

plt.ylim(50,140)
major_ticks = np.arange(50, 151, 20)
minor_ticks = np.arange(50, 151, 5)

ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

plt.ylabel('Frecventa Cardiaca')

plt.xticks([])

ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)

plt.title(r'Evolutie \textbf{cardio} \underline{individuala} intre intre cele doua grupuri')
plt.legend()

#plt.show()
plt.savefig('./grafice/cardio_individual.png')
