from typing import List, Any

import pandas as pd
import xlrd
import os
import datetime
from datetime import timedelta
import calendar

from pandas import ExcelFile

global inp, skubl, skudep, skudim, skumach, hopmach
indent = 1
days_remaining: List[Any] = []


def input():
    # Taking input of KM Tracker
    path = pd.ExcelFile(root[0] + "\\Output\\execle_gen_" + str(datetime.date.today()) + ".xlsx")
    cols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    inp = pd.read_excel(path, "Sheet1", usecols=cols)

    # Taking SKU-Blend Correlation
    path = pd.ExcelFile(root[0] + "\\input\\SKU - Blend Correlation, SKU details.xlsx")
    cols = [1, 3]
    skubl = pd.read_excel(path, "Sheet1", skiprows=1, usecols=cols)

    # Taking SKU-Depo Correlation
    path = pd.ExcelFile(root[0] + "\\input\\SKU - Depot Correlation.xlsx")
    cols = [2, 3]
    skudep = pd.read_excel(path, "Sheet1", skiprows=2, usecols=cols)

    # Taking SKU Dimensions
    path = pd.ExcelFile(root[0] + "\\input\\SKU dimensions.xlsx")
    cols = [2, 4, 5, 6, 10, 11, 12]
    skudim = pd.read_excel(path, "SKU dimensions", skiprows=25, usecols=cols)
    skudim = skudim[skudim["Select your PC & Blank before Updating"] == "PULP"]

    # Taking SKU-Machine dependency
    path = pd.ExcelFile(root[0] + "\\input\\SKU wise - Machine wise capacities.xlsx")
    cols = [0, 2, 4, 5, 6, 7]
    skumach = pd.read_excel(path, "Sheet3", skiprows=5, usecols=cols)

    # Taking Hopper-Machine Dependency
    path = pd.ExcelFile(root[0] + "\\input\\Hopper - machine correlation.xlsx")
    cols = [1, 2]
    hopmach = pd.read_excel(path, "Sheet1", skiprows=1, usecols=cols)


# Getting current working directory
root = os.getcwd()
root = root.split("\\Scheduler")  # to get one file up
os.chdir(root[0])

input()

tod = str(datetime.date.today())
month = int(tod.split('-')[1])
year = int(tod.split('-')[0])
day = int(tod.split('-')[2])

# Getting days remaining
if day > 14:
    indent = 2
i = [day, month]
tod = datetime.date.today()
if indent == 1:
    while i[0] < 15:
        days_remaining = days_remaining + [tod]
        tod += timedelta(days=1)
        i[0] = int(str(tod).split('-')[2])
        i[1] = int(str(tod).split('-')[1])
else:
    temp = calendar.monthrange(year, month)
    while i[0] <= temp[1] and i[1] == month:
        days_remaining = days_remaining + [tod]
        tod += timedelta(days=1)
        i[0] = int(str(tod).split('-')[2])
        i[1] = int(str(tod).split('-')[1])

holiday_list = []

# Get list of holidays at in v2
temp = days_remaining
for n in days_remaining:
    if n in holiday_list:
        temp.remove(n)

