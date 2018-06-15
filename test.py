import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def draw_label(ax, rects, names):
    """TODO: Docstring for draw_label.

    :rect: TODO
    :returns: TODO

    """
    for i, rect in enumerate(rects):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2.0,
                1.05*height, '%s' % names[i][:-6],
                ha='center', va='bottom')


df = pd.read_excel('./Datedisertatie.xlsx')
possitive_bar_list = []
negative_bar_list = []
possitive_x_names = []
negative_x_names = []

columns_name = df.columns.values.tolist()

print('There are:', len(columns_name), ' columns')
for i in range(1, len(df.columns)-2, 4):
    print(columns_name[i], ':', columns_name[i+2])
    dif = df.iloc[-1, i] - df.iloc[-1, i+2]
    if (dif > 0):
        possitive_bar_list.append(dif)
        possitive_x_names.append(str(columns_name[i]))
    else:
        negative_bar_list.append(dif)
        negative_x_names.append(str(columns_name[i]))

width = 0.3
x1 = 2*np.arange(len(possitive_bar_list))
x2 = 2*np.arange(len(negative_bar_list)) + 1
fig, ax = plt.subplots()
positive_rects = ax.bar(x1, possitive_bar_list, width=width, alpha=0.8,
                        color='b', label='Positive mean')
negative_rects = ax.bar(x2, negative_bar_list, width=width, alpha=0.8,
                        color='r', label='Negative mean')

draw_label(ax, positive_rects, possitive_x_names)
draw_label(ax, negative_rects, negative_x_names)
plt.show()
