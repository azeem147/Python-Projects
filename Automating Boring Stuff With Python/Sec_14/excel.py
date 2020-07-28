import openpyxl
import os
os.chdir('F:\\Python Projects\\Automating Boring Stuff With Python\\Sec_14')
workbook = openpyxl.load_workbook('example.xlsx')
print(workbook.get_sheet_names())
sheet = workbook.get_sheet_by_name('Sheet1')
print(str(sheet['A1'].value))
print(sheet['B1'].value)
print(sheet['C1'].value)
