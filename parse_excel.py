import xlrd	
workbook = xlrd.open_workbook('parse.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')

nameArray= [] # array of names
cellArray = [] # array of cells adopted
amountArray = [] # amount donated

i = 1
for row in range(worksheet.nrows-1):
	nameArray.append(worksheet.cell(i,0).value)
	cellArray.append(worksheet.cell(i,1).value)
	amountArray.append(worksheet.cell(i,2).value)
	i = i+1




for x in len(nameArray):
	print( "{} adopted cell {} with an amount of ${}". format(nameArray[x],  cellArray[x], amountArray[x])
	x = x+1