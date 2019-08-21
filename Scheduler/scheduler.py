import pandas as pd
import xlrd
import os

global df

a = os.getcwd()
a = a.split("\\Scheduler")          #to get one file up
os.chdir(a[0])
xls = pd.ExcelFile(os.getcwd() + "\\Output\\ttrucko.xlsx")

cols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
df1 = pd.read_excel(xls, "Sheet1", usecols=cols)
print(df1)
df1 = df1[df1.valid == 1]


