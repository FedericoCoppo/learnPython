"""
the script is used to search and delete specific column of all sheet in a Excel
"""

import pandas as pd
import xlrd
import sys

print (sys.argv[1])
fileName = sys.argv[1]   # keep file name from stdin

xls = xlrd.open_workbook(fileName, on_demand=True)
sheet_name_list = xls.sheet_names()

# just to print the sheetNames
for sheetName in sheet_name_list:
	print(sheetName, flush=True)

writer = pd.ExcelWriter(fileName, engine = 'xlsxwriter')

outDf = {}
lst = []
i = 0

for sheetName in sheet_name_list:
	lst.append(i)                       # sheet list creation
	i = i + 1
	sizeList = i

print(lst, flush=True)
masterdf = pd.read_excel(fileName, lst )

for k in range(sizeList):
	if 'Time[s]' in masterdf[k] and 'RPM' in masterdf[k] :
		outDf[k] = masterdf[k].drop(masterdf[k].columns[[2, 3]], axis=1)
		print("delete RMP and Time[s] from %s sheet!" % sheetName, flush=True)
		outDf[k].to_excel(writer, sheet_name = sheet_name_list[k], index=False)    # update new excel
	else:
		print("column [Time[s]] or [RPM] not found", flush=True)

writer.save()
writer.close()
print("%s file updated !" % fileName, flush=True)
