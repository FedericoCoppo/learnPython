# Author: Coppo Federico 
# Description: the script plot data from excel using matplotlib all the 
# column defined into EnableList (1st col should be the sample time)
 
import xlrd
from datetime import date
import matplotlib.pyplot as plt

#
# The function search a string label into a datataset list.
#
def find_enable_label(labelString, enableList):
	found = False
	for i in range(0, len(enableList)):  
		if enableList[i] == labelString:
			found = True
			print("found", labelString)
	
	return found
		
print("date:", date.today())

# open file
workbook = xlrd.open_workbook('datasetExample.xlsx')

# opening the sheet 
worksheet= workbook.sheet_by_name('dataset1')		

#debug info
colNum = worksheet.ncols
print("number of column: % 2d\n" %(colNum)) 
rowNum = worksheet.nrows
print("number of raw: % 2d\n" %(rowNum)) 

# create list of string to be used
labelList = []
labelUnitList = []

# list of column that will be printed
EnableList = ['Speed1', 'Speed3', 'Speed4'];

# read the measure and the measure unit
for i in range(0, worksheet.ncols):        
	labelList.append(worksheet.row_values(0, i))
	labelUnitList.append(worksheet.row_values(1, i))

# time extract
	x = worksheet.col_values(0)  # column i (time)
	X = x[4:rowNum + 2]          # only data measurement
	
for i in range(1, colNum):
	if (find_enable_label(labelList[0][i],EnableList)):
		y = worksheet.col_values(i)  # 
		Y = y[4:rowNum + 2]
		plt.plot(X,Y, label = (labelList[0][i] + labelUnitList[0][i] )) # plot the column data 

plt.xlabel('time [s]')
plt.legend(loc='best')
plt.grid()
plt.show()
