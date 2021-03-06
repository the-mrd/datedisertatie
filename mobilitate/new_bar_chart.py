#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc


def normalize(df):
    df_norm = (df - df.mean()) / (df.max() - df.min())
    return df_norm

def autolabel(rects, ax, names, bottom=False):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for i, rect in enumerate(rects):
        if bottom == False:
            height = rect.get_height()
        else:
            height = rect.get_height()*(-1)

        # Fraction of axis height taken up by this rectangle
        p_height = (height / y_height)


        # If we can fit the label above the column, do that;
        # otherwise, put it inside the column.
        if p_height > 0.95: # arbitrary; 95% looked good to me.
            label_position = height - (y_height * 0.05)
        else:
            label_position = height - (y_height * 0.01)

        ax.text(rect.get_x() + rect.get_width()/2., label_position,
                '%s' % names[i][:-9],
                ha='center', va='bottom')

def draw_label(ax, rects, names, max_height):
    """TODO: Docstring for draw_label.

    :rect: TODO
    :returns: TODO

    """
    for i, rect in enumerate(rects):
        height = rect.get_height()
        if height >= max_height:
            factor=1
        else:
            factor=1.05

        ax.text(rect.get_x() + rect.get_width()/2.0,
                factor*height, '%s' % names[i][:-9],
                ha='center', va='bottom')

def create_graph(xls_path,start_pos, end_pos_offset, step, cmp_offset, color1, color2,percent,label1, label2, titlu, outfile):
	#df = pd.read_excel('./Datedisertatie.xlsx')
	df = pd.read_excel(xls_path)

	possitive_bar_list = []
	negative_bar_list = []
	possitive_x_names = []
	negative_x_names = []

	rc('text', usetex=True)

	plt.rcParams['text.usetex'] = True
	plt.rcParams['text.latex.unicode'] = True


	columns_name = df.columns.values.tolist()
	possitive_bar_list=[]
	negative_bar_list=[]

	print('There are:', len(columns_name), ' columns in xls file: ',xls_path)

	for i in range(start_pos, len(df.columns)-end_pos_offset, step):
		print('Comparing:', columns_name[i], ' and ', columns_name[i+1])
		if percent == True:
			dif = (df.iloc[-1, i+cmp_offset] - df.iloc[-1, i])/df.iloc[-1, i]*100
		else:
			dif = df.iloc[-1, i+cmp_offset] - df.iloc[-1, i]

		if (dif > 0):
			possitive_bar_list.append(dif)
			#possitive_x_names.append(u' '.join((columns_name[i])).encode('utf-8').strip())
			possitive_x_names.append(str(columns_name[i]))
		else:
			negative_bar_list.append(dif)
			#negative_x_names.append(u' '.join((columns_name[i])).encode('utf-8').strip())
			negative_x_names.append(str(columns_name[i]))

	    #maxim=max(possitive_bar_list)

	width = 0.3
	x1 = 2*np.arange(len(possitive_bar_list))
	x2 = 2*np.arange(len(negative_bar_list)) + 1
	fig, ax = plt.subplots(figsize=(12,5), dpi=100) #portrait paper

	#figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

	positive_rects = ax.bar(x1, possitive_bar_list, width=width, alpha=0.8,
				color=color1, label=label1)
	negative_rects = ax.bar(x2, negative_bar_list, width=width, alpha=0.8,
				color=color2, label=label2)

	autolabel(positive_rects, ax, possitive_x_names)
	autolabel(negative_rects, ax, negative_x_names, bottom=True)
	plt.title(titlu)
	plt.legend()
	plt.savefig(outfile)
	plt.show()

xls='./mobilitate.xlsx'
start=1
end=2
step=4
compare_offset=1
c1='b'
c2='r'
percent=True
label1='Imbunatatire'
label2='Degradare'
title=r'Diferenta \textit{in medie} dintre Testarea \textbf{Finala} si cea \textbf{Initiala} de mobilitate in grupul IE'
outf='delme.png'

create_graph(xls, start, end, step, compare_offset, c1, c2, percent, label1, label2, title, outf)
