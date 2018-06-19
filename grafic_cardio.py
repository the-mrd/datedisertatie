
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

for i in range(len(x)//2 - 1):
	if y[i*2] > y[i*2 + 1]:
		mymark = 'bv--'
	else:
		mymark = 'b^--'
	
	ax.plot(x[i*2:i*2+2], y[i*2:i*2+2], mymark)


ax.plot(x[i*2:i*2+2], y[i*2:i*2+2], mymark, label='Grup PG')
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
	if y[i*2] > y[i*2 + 1]:
		mymark = 'r1--'
	else:
		mymark = 'r2--'
	ax.plot(x[i*2:i*2+2], y[i*2:i*2+2], mymark)

ax.plot(x[i*2:i*2+2], y[i*2:i*2+2], mymark, label='Grup IE')
plt.xticks([])
plt.title(r'Evolutie \textbf{cardio} \underline{individuala} intre intre cele doua grupuri')
plt.legend()
#plt.show()
plt.savefig('./grafice/cardio_individual.png')
