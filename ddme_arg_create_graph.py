#!/usr/bin/env python3
import create_titf_graphs
"""
# Mobilitate Medie PG
xls='./mobilitate/mobilitate.xlsx'
start=1
end=2
step=4
compare_offset=1
c1='g'
c2='r'
percent=True
label1='Crestere'
label2='Scadere'
title=r'Diferenta \textit{in medie} dintre Testarea \textbf{Finala} si cea \textbf{Initiala} de mobilitate in grupul PG'
outf='grafice/mobilitate_medie_PG.png'
create_graphs.create_graph(xls, start, end, step, compare_offset, c1, c2, percent, label1, label2, title, outf)

# Mobilitate Medie IE
xls='./mobilitate/mobilitate.xlsx'
start=3
end=1
step=4
compare_offset=1
c1='g'
c2='r'
percent=True
label1='Crestere'
label2='Scadere'
title=r'Diferenta \textit{in medie} dintre Testarea \textbf{Finala} si cea \textbf{Initiala} de mobilitate in grupul IE'
outf='grafice/mobilitate_medie_IE.png'
create_graphs.create_graph(xls, start, end, step, compare_offset, c1, c2, percent, label1, label2, title, outf)
# Mobilitate Medie TI
xls='./mobilitate/mobilitate.xlsx'
start=1
end=2
step=4
compare_offset=2
c1='tab:orange'
c2='tab:purple'
percent=True
label1='Grup PG'
label2='Grup IE'
title=r'Diferenta \textit{in medie} la \textbf{Testarea \underline{Initiala} de mobilitate} intre cele doua grupuri'
outf='grafice/mobilitate_medie_TI.png'
create_titf_graphs.create_graph(xls, start, end, step, compare_offset, c1, c2, percent, label1, label2, title, outf)

# Mobilitate Medie TF
xls='./mobilitate/mobilitate.xlsx'
start=2
end=2
step=4
compare_offset=2
c1='tab:orange'
c2='tab:purple'
percent=True
label1='Grup PG'
label2='Grup IE'
title=r'Diferenta \textit{in medie} la \textbf{Testarea \underline{Finala} de mobilitate} intre cele doua grupuri'
outf='grafice/mobilitate_medie_TF.png'
create_titf_graphs.create_graph(xls, start, end, step, compare_offset, c1, c2, percent, label1, label2, title, outf)

# Cardio
xls='./cardio/cardio.xlsx'
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
create_graphs.create_graph(xls, start, end, step, compare_offset, c1, c2, percent, label1, label2, title, outf)
"""

"""
# Capacitate Coordinativa Medie PG
xls='./capacitate_coordonativa/capacitate_coordonativa.xlsx'
start=1
end=2
step=4
compare_offset=1
c1='g'
c2='r'
percent=True
label1='Crestere'
label2='Scadere'
title=r'Diferenta \textit{in medie} dintre Testarea \textbf{Finala} si cea \textbf{Initiala} de Capacitate Coordinativa in grupul PG'
outf='grafice/capac_medie_PG.png'
create_graphs.create_graph(xls, start, end, step, compare_offset, c1, c2, percent, label1, label2, title, outf)

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
"""

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
