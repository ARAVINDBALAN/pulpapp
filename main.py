import tkinter as tk
import os,sys,subprocess
import shutil
from pathlib import Path
#from tkinter import *
import pandas as pd
from tkinter import filedialog,Grid,N,S,W,E,messagebox,ttk
from datetime import date
today = date.today()
print(today)
root= tk.Tk()
style = ttk.Style()

root.title("Pulp App")
root.geometry("1000x450")
#Grid.rowconfigure(root, 0, weight=3)
#Grid.columnconfigure(root, 0, weight=1)

tk.Label(text=today).grid()
#canvas1 = tk.Canvas(root, width = 1500, height = 500, bg = 'lightsteelblue')
#canvas1.grid(sticky="nsew")
#canvas1.grid(row=0, column=0, sticky=N+S+E+W)

def open_file(filename):
    if (sys.platform == "win32"):
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])



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


def modify_machine_hopper(file):
    global machine_hopper
    op=os.getcwd()
    try:
        os.mkdir("Input")
        os.chdir(os.getcwd()+"/Input")
        import_file_path = filedialog.askopenfilename(title="Add/edit")
        print(import_file_path)
        shutil.copy(import_file_path,os.getcwd())
    except FileExistsError:
        if(os.path.exists(op+"/Input/"+file)):
            os.chdir(op+"/Input")
            open_file(file)
        else:
            os.chdir(os.getcwd()+"/Input")
            import_file_path = filedialog.askopenfilename(title="Add/edit")
            shutil.copy(import_file_path,os.getcwd())
    os.chdir(op)






def getExcel():
    global df  
    import_file_path = filedialog.askopenfilename(title="open")
    xls = pd.ExcelFile(import_file_path)
    cols = [0,1,2,6,51,52,57,58,59,60,130,131]
    df = pd.read_excel(xls,"MAIN DATA",skiprows=4,usecols=cols)
    df = df[df.PC=="PULP"]
    df = df[df["Balance Dispatch"]=="Dispatch"]
    df = df[df.Validity=="Valid"]
    print(df)
    op=os.getcwd()
    try:
        os.mkdir("Output")
        os.chdir(os.getcwd()+"//Output")
    except FileExistsError:
        os.chdir(os.getcwd()+"//Output")
    name_of_created = "execle_gen_"+str(date.today())+".xlsx"
    df[df.PC=='PULP'].to_excel(name_of_created)
    os.chdir(op)
style.configure("inp",font = ('calibri', 10, 'bold'))




search_sku_entry = tk.Entry(root)
search_sku_entry.grid(column=0,row=0)

search_sku_entry_button = tk.Button(text="Search",command=search_sku)
search_sku_entry_button.grid(column=1,row=0)
kmtraderButton_Excel = tk.Button(text='Import KM Trader ', command = getExcel, width=24,bg='green', fg='white', font=('helvetica', 12, 'bold')).grid(pady=5)
IndentButton_Excel = tk.Button(text='Import Indent ', command = getExcel,width=24, bg='green', fg='white', font=('helvetica', 12, 'bold')).grid(pady=5)
Button_Excel = tk.Button(text='Import truck dimensions ', command = getExcel,width=24, bg='green', fg='white', font=('helvetica', 12, 'bold')).grid(pady=5)
kmButton_Excel = tk.Button(text='Add/Modify SKUs', command = lambda: modify_machine_hopper("SKU wise - Machine wise capacities.xlsx"), bg='green', width=24,fg='white', font=('helvetica', 12, 'bold')).grid(pady=5)
kmButton_Excel = tk.Button(text='Add/Modify Machines', command =lambda :modify_machine_hopper("Hopper - machine correlation.xlsx"), bg='green',width=24, fg='white', font=('helvetica', 12, 'bold')).grid(pady=5)

#canvas1.create_window(1000,100,window=kmtraderButton_Excel)
#root.rowconfigure(1,weight=1)
root.mainloop()
