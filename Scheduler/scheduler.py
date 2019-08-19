import pandas
import xlrd
global df
xls = pd.ExcelFile(import_file_path)

sched={}
i=0
while i<15:
    i+=1
    sched[i]=[]