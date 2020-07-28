import PyPDF2
import os
print(os.getcwd())
os.chdir('F:\\Python Projects\\Automating Boring Stuff With Python\\Sec_14')
print(os.getcwd())
pdfFile = open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)
page = reader.getPage(0)
print(page.extractText())
