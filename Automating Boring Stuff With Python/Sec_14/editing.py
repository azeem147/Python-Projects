import openpyxl
wb = openpyxl.Workbook()
wb.get_sheet_names()
sheet = wb.get_sheet_by_name('Sheet')
print(sheet['A1'].value == None)
sheet['A1'] = 42
sheet['A2'] = 'Hello'
wb.save('example1.xlsx')
