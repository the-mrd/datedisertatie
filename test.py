import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./Datedisertatie.xlsx')

bar_list=[]
x_names = []
columns_name = df.columns.values.tolist()
for i in range(1, len(df.columns)-2, 4):
    dif = df.iloc[-1,i]-df.iloc[-1,i+2]
    if (abs(dif) > 50):
        bar_list.append(dif)
        x_names.append(str(columns_name[i]))

print(len(columns_name))
print(df.describe())
x = range(len(bar_list))
plt.bar(x_names, bar_list, width=2.0)

plt.show()

