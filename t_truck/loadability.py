import pandas as pd
truck_capacity = {"16":[16000,28560000],"145":[14500,58540000],"9":[9000,25870000],"65":[6500,35000000]}
def calculate_loadability(truck_key,sku_list):
    weight = 0
    volume = 0
    det = truck_capacity[truck_key]
    sku_det = sku_list[1:]
    for i in range(len(sku_det)):
        weight += (find_weight(sku_det[i][0])*sku_det[i][1])
        volume += (find_volume(sku_det[i][0])*sku_det[i][1])
    per_weight = weight/det[0]*100
    per_vol = volume/det[1]*100
    if(per_vol>=per_weight):
        l = [per_vol,"volume"]
        return l
    else : 
        l = [per_weight,"weight"]
        return l

def find_weight(sku_det):
    df = pd.read_excel("SKU dimensions.xlsx",sheet="sheet1")
    row = df[df["SKU CODE"]==sku_det]
    return row[1]

def find_volume(sku_det):
    df = pd.read_excel("SKU dimensions.xlsx",sheet="sheet1")
    row = df[df["SKU CODE"]==sku_det]
    return row[2]

  
  
