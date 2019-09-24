from typing import List, Any

import pandas as pd
import os
import datetime
from datetime import timedelta
from pandas import Series
import calendar
from pandas import ExcelFile
class NOSKU(Exception):
    pass

def uniquelist(list1):
    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
            # print list
    return unique_list

def get_index_of_list(dict,item):
    for n in dict.items():
        if item in n[1]:
            return n[0]
    raise NOSKU


op = {"Plan Day": [], "Item": [], "Item Desc": [], "Blend": [], "Hopper": [], "ResId": [], "Shift-A": [], "Shift-B": [],
      "Shift-C": []}
work = {"SKU": [], "Depo": [], "Machine": [], "TTC": [], "Quant": []}
op = pd.DataFrame(op)
op.set_index(["Plan Day", "Item"])
work = pd.DataFrame(work)
work.set_index(["SKU", "Depo"])
indent = "L1 Indent"
days_remaining: List[Any] = []

# Getting current working directory
root = os.getcwd()
root = root.split("\\Scheduler")  # to get one file up
os.chdir(root[0])

# Taking input of KM Tracker
path = pd.ExcelFile(root[0] + "\\Output\\execle_gen_" + str(datetime.date.today()) + ".xlsx")
cols = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
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
cols = [0, 1, 2, 4, 5, 6, 7]
skumach = pd.read_excel(path, "Sheet3", skiprows=5, usecols=cols)

# Taking Hopper-Machine Dependency
path = pd.ExcelFile(root[0] + "\\input\\Hopper - machine correlation.xlsx")
cols = [1, 2]
hopmach = pd.read_excel(path, "Sheet1", skiprows=1, usecols=cols)

tod = str(datetime.date.today())
month = int(tod.split('-')[1])
year = int(tod.split('-')[0])
day = int(tod.split('-')[2])

# Getting days remaining
if day > 15:
    indent = "L2 Indent"

i = [day, month]
tod = datetime.date.today()
if indent == "L1 Indent":
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
days_remaining = temp

# Getting time to complete depo wise
skumach["MACHINE / WORK CENTER "] = pd.Series(skumach["MACHINE / WORK CENTER "]).fillna(method='ffill')
skumach.set_index(["MACHINE / WORK CENTER ", "SKU CODE"])
skmh = {}

# Getting list of machines
for n in skumach.index:
    skmh[skumach["MACHINE / WORK CENTER "][n]] = []

# Getting list of SKU for each machine
for n in skumach.index:
    skmh[skumach["MACHINE / WORK CENTER "][n]] = skmh[skumach["MACHINE / WORK CENTER "][n]] + [skumach["SKU CODE"][n]]

# Getting rates
for n in inp.index:
    quant = inp[indent][n]
    if quant != 0:
        temp = {"SKU": [], "Depo": [], "Machine": [], "TTC": [], "Quant": []}
        mat = inp["MATERIAL"][n]
        try:
            mach = get_index_of_list(skmh,mat)
        except NOSKU:
            inp.drop(n)
            continue
        filter1 = skumach["MACHINE / WORK CENTER "] == mach
        filter2 = skumach["SKU CODE"] == mat
        rate = (skumach.where(filter1 & filter2,inplace=False))
        rate = rate.dropna()
        rate = int(list(rate["OUTPUT PER HOUR"])[0])
        ttc = quant/rate
        temp["SKU"] = mat
        temp["Depo"] = inp["DEPO"][n]
        temp["Machine"] = mach
        temp["TTC"] = ttc
        temp["Quant"] = quant
        work = work.append(temp,verify_integrity=True,ignore_index=True)

work.sort_values(by="TTC", inplace=True)


print(work)

