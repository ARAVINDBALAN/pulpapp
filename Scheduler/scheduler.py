import pandas as pd
import xlrd
import os
from datetime import date

global df

a = os.getcwd()
a = a.split("\\Scheduler")  # to get one file up
os.chdir(a[0])
xls = pd.ExcelFile(os.getcwd() + "\\Output\\execle_gen_" + str(date.today()) + ".xlsx")

cols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
df = pd.read_excel(xls, "Sheet1", usecols=cols)

