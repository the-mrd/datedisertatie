#!/usr/bin/env python3

import create_graphs
# Capacitate Coordinativa Medie PG

xls='./capacitate_coordonativa/capacitate_coordonativa.xlsx'
start=3
end=1
step=4
compare_offset=1
c1='g'
c2='r'
percent=True
label1='Crestere'
label2='Scadere'
title=r'Diferenta \textit{in medie} dintre Testarea \textbf{Finala} si cea \textbf{Initiala} de Capacitate Coordinativa in grupul IE'
outf='grafice/capac_medie_IE.png'
create_graphs.create_graph(xls, start, end, step, compare_offset, c1, c2, percent, label1, label2, title, outf)

