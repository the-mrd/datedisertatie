import pandas as pd
import matplotlib.pyplot as plt

def draw_label(rects, names):
    """TODO: Docstring for draw_label.

    :rect: TODO
    :returns: TODO

    """
    for i, rect in enumerate(rects):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2.0,
                1.05*height, '%s' %names[i],
                ha='center', va='bottom')

df = pd.read_excel('./Datedisertatie.xlsx')

bar_list=[]
x_names = []
columns_name = df.columns.values.tolist()
for i in range(1, len(df.columns)-2, 4):
    dif = df.iloc[-1,i]-df.iloc[-1,i+2]
    if (abs(dif) > 10):
        bar_list.append(dif)
        x_names.append(str(columns_name[i]))

print(len(columns_name))
print(df.describe())
x = range(len(bar_list))
# plt.figure(figsize=(12, 8))
fig, ax = plt.subplots()
rects = ax.bar(x, bar_list, width=0.2, alpha=0.8)
draw_label(rects, x_names)
plt.show()
