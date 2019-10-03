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

def addtomach(schedule, cursku, mach, timetocomp, skumach, shift):
    listofmach = []
    for n in schedule:
        if len(schedule[mach]) < 3:



def uniquelist(list1):
    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def get_index_of_list(dict, item, skipmachine =()):
    for n in dict.items():
        if n[0] in skipmachine:
            continue
        if item in n[1]:
            return n[0]
    raise NOSKU


 op = {"Plan Day": [], "Item": [], "Item Desc": [], "Blend": [], "Hopper": [], "ResId": [], "Shift-A": [], "Shift-B": [],
      "Shift-C": []}
timetocomp = {"SKU": [], "Depo": [], "Machine": [], "TTC": [], "Quant": []}
op = pd.DataFrame(op)
op.set_index(["Plan Day", "Item"])
timetocomp = pd.DataFrame(timetocomp)
timetocomp.set_index(["SKU", "Depo"])
indent = "L1 Indent"
days_remaining: List[Any] = []


# Getting current working directory
root = os.getcwd()
root = root.split("\\Scheduler")  # to get one file up
os.chdir(root[0])

path = pd.ExcelFile(root[0] + "\\input\\output_from_km_dimension.xlsx")
stage1op = pd.read_excel(path)
# # Taking input of KM Tracker
# path = pd.ExcelFile(root[0] + "\\Output\\execle_gen_" + str(datetime.date.today()) + ".xlsx")
# cols = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# inp = pd.read_excel(path, "Sheet1", usecols=cols)

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

#machine SKU Co-relations
skumach["MACHINE / WORK CENTER "] = pd.Series(skumach["MACHINE / WORK CENTER "]).fillna(method='ffill')
skmh = {}

# Getting list of machines
for n in skumach.index:
    skmh[skumach["MACHINE / WORK CENTER "][n]] = []

# Getting list of SKU for each machine
for n in skumach.index:
    skmh[skumach["MACHINE / WORK CENTER "][n]] = skmh[skumach["MACHINE / WORK CENTER "][n]] + [skumach["SKU CODE"][n]]

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

# Getting rates
for n in stage1op.index:
    quant = stage1op[indent][n]
    if quant != 0:
        temp = {"SKU": [], "Depo": [], "Machine": [], "TTC": [], "Quant": []}
        mat = stage1op["MATERIAL"][n]
        try:
            mach = get_index_of_list(skmh,mat)
        except NOSKU:
            stage1op.drop(n,inplace=True)
            continue
        filter1 = skumach["MACHINE / WORK CENTER "] == mach
        filter2 = skumach["SKU CODE"] == mat
        rate = (skumach.where(filter1 & filter2, inplace=False))
        rate = rate.dropna()
        rate = int(list(rate["OUTPUT PER HOUR"])[0])
        ttc = quant/rate
        temp["SKU"] = mat
        temp["Depo"] = stage1op["DEPO"][n]
        temp["Machine"] = mach
        temp["TTC"] = ttc
        temp["Quant"] = quant
        timetocomp = timetocomp.append(temp, verify_integrity=True, ignore_index=True)

timetocomp.sort_values(by="TTC", inplace=True)
timetocomp.reset_index(drop=True)
schedule = {}
machqueue = {}
for n in list(skmh.items()):
    schedule[n[0]] = [["No item","No item","No item"]]*len(days_remaining)
    machqueue[n[0]] = []
quant_to_prod = {}
for n in timetocomp.index:
    quant_to_prod[timetocomp["SKU"][n]+" "+timetocomp["Depo"][n]] = timetocomp["Quant"][n]
print(schedule)
# print(machqueue)
# print(quant_to_prod)
# print(len(quant_to_prod))

i = days_remaining[0]
while i in days_remaining:
    ind = list(timetocomp.index)
    j = 0
    shift = 1
    while True:
        curdepo = str(timetocomp["Depo"][ind[j]])
        print(curdepo)
        temp = (timetocomp.groupby("Depo"))
        temp = temp.get_group(curdepo)
        temp = temp.sort_values("TTC")
        for k in temp.index:
            cursku = temp["SKU"][k]
            mach = temp["Machine"][k]
            schedule = addtomach(schedule, cursku, mach, timetocomp, skumach, shift)
        if shift > 3:
            i += timedelta(days=1)