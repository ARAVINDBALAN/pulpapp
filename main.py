import tkinter as tk
import os
#from tkinter import *
import pandas as pd
from tkinter import filedialog,Grid,N,S,W,E,messagebox
from datetime import date
today = date.today()
print(today)
root= tk.Tk()
root.title("Pulp App")
root.geometry("1000x450")
#Grid.rowconfigure(root, 0, weight=3)
Grid.columnconfigure(root, 0, weight=1)
tk.Label(text="Date : ").grid(row=2,column=10)
tk.Label(text=today).grid(row = 2, column = 11)
#canvas1 = tk.Canvas(root, width = 1500, height = 500, bg = 'lightsteelblue')
#canvas1.grid(sticky="nsew")
#canvas1.grid(row=0, column=0, sticky=N+S+E+W)

def search_sku():
    #var = StringVar()
    sku = search_sku_entry.get()
    if(sku==""):
        messagebox.showerror("Sku null","no sku presented")
        return 
    else:
        print(sku)
        sku_name = df['MATERIAL']
        if(sku in sku_name[1]):
            print(sku_name[1])
        else:
            print("not found")
        print(sku_name)



def getExcel():
    global df  
    import_file_path = filedialog.askopenfilename(title="open")
    xls = pd.ExcelFile(import_file_path)
    cols = [0,1,2,6,13,16,17,51,52,57,58,59,60,130,131]
    df = pd.read_excel(xls,"MAIN DATA",skiprows=4,usecols=cols)
    df = df[df.PC=="PULP"]
    df = df[df["Balance Dispatch"]=="Dispatch"]
    df = df[df.Validity=="Valid"]
    df["L2 Indent"]=df["INDENT KG"]-df["L1 Indent"]
    print(df)
    a = os.getcwd()
    os.chdir(a+"\\Output")
    name_of_created = "execle_gen_"+str(date.today())+".xlsx"
    df[df.PC=='PULP'].to_excel(name_of_created)
search_sku_entry = tk.Entry(root)
search_sku_entry.grid()
search_sku_entry_button = tk.Button(text="Search",command=search_sku).grid(row=4)
kmtraderButton_Excel = tk.Button(text='Import KM Trader ', command = getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold')).grid(row=7,column=10)
IndentButton_Excel = tk.Button(text='Import Indent ', command = getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold')).grid(column=10)
Button_Excel = tk.Button(text='Import KM Trader ', command = getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold')).grid(column=10)
kmButton_Excel = tk.Button(text='Import KM Trader ', command = getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold')).grid(column=10)
#canvas1.create_window(1000,100,window=kmtraderButton_Excel)
#root.rowconfigure(1,weight=1)
root.mainloop()
