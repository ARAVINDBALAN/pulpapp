import pandas as pd
import xlrd
import os
a=os.getcwd()
a=a.split("\\Scheduler")
os.chdir(a[0])
global df
xls = pd.ExcelFile(os.getcwd()+"\\Output\\ttrucko.xlsx")
cols=[0,1,2,3,4,5,6,7,8,9]
df = pd.read_excel(xls,"Sheet1",usecols=cols)
print(df)
i=0,
sched={}
while i<15:
    i+=1
    sched[i]=[]