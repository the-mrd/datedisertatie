#!/usr/bin/env python3

import create_titf_graphs

xls='./capacitate_coordonativa/capacitate_coordonativa.xlsx'
start=1
end=2
step=4
compare_offset=2
c1='tab:orange'
c2='tab:purple'
percent=True
label1='Grup PG'
label2='Grup IE'
title=r'Diferenta \textit{in medie} la \textbf{Testarea \underline{Initiala} de Capacitate Coordinativa} intre cele doua grupuri'
outf='grafice/capac_medie_TI.png'
create_titf_graphs.create_graph(xls, start, end, step, compare_offset, c1, c2, percent, label1, label2, title, outf)

xls='./capacitate_coordonativa/capacitate_coordonativa.xlsx'
start=2
end=1
step=4
compare_offset=2
c1='tab:orange'
c2='tab:purple'
percent=True
label1='Grup PG'
label2='Grup IE'
title=r'Diferenta \textit{in medie} la \textbf{Testarea \underline{Finala} de Capacitate Coordinativa} intre cele doua grupuri'
outf='grafice/capac_medie_TF.png'
create_titf_graphs.create_graph(xls, start, end, step, compare_offset, c1, c2, percent, label1, label2, title, outf)
