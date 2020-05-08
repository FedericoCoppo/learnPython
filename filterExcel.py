
"""
F.C.

The script is used to manag big excel data:
	it allow to sample defined number of row in excel 
	with big amount of data swapped between different sheet
	The float data with comma notation are changed to dot notation
	
	the output could be directly managed by google sheet for graph plotting
"""

import pandas as pd
import xlrd
import sys

# param
SAMPLE_STEP = 1000 # this parameter is the step used to sample row in excel

print (sys.argv[1])
fileName = sys.argv[1]   # keep file name from stdin
fileName_out = "Filt" + fileName
xls = xlrd.open_workbook(fileName, on_demand=True)
sheet_name_list = xls.sheet_names()

# just to print the sheetNames
for sheetName in sheet_name_list:
	print(sheetName, flush=True)

writer = pd.ExcelWriter(fileName_out, engine = 'xlsxwriter')

#outDf = {}
lst = []
i = 0

for sheetName in sheet_name_list:
	lst.append(i)                       # sheet list creation
	i = i + 1
	sizeList = i

print(lst, flush=True)
masterdf = pd.read_excel(fileName, lst)

column_names = masterdf[0].columns
print(column_names)
outDf = pd.DataFrame(columns = column_names)

# for each sheet
for k in range(sizeList):
	df = masterdf[k]
	
	count_row = df.shape[0]  # gives number of row count
	count_col = df.shape[1]  # gives number of col count
	for i in range(0, count_row, SAMPLE_STEP):
		for j in column_names:
			df[j]= df[j].astype(str)
			df[j]= df[j].astype(str)
		df.apply(lambda x: x.str.replace(',','.'))
		outDf = outDf.append(df.iloc[[i]], sort=False)
		
print(outDf.head())
outDf.to_excel(writer, sheet_name = sheet_name_list[k], index=False) 
writer.save()
writer.close()
print("%s file has been updated updated !" % fileName_out, flush=True)