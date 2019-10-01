import pandas as pd
import os
import testui 
import math
#inputs are main data after stage one and no of days_remaining

truck_capacity = {160:[16000,28560000000],145:[14500,58540000000],90:[9000,25870000000],65:[6500,35000000000]}
truck_pref=[["KL01",160],["KL01",90],["AP01",65],["AP03",65],["GO01",160],["KK01",160],["KK02",160],["KK02",145],["TN01",160],["TN02",90],["TN03",90],["MH01",65],["MH02",145],["MH04",160]]
#depo=["KL01","AP01","AP03","GO01","KK01","KK02","TN01","TN02","TN03","MH01","MH02","MH04"]
depo_qt=[None]
'''function to check if indent is from l1 or l2 when scheduling '''
print(testui.li)

def tenative(datelist):
    no_of_trucks_volume = 0
    remaining_trucks_volume = 0
    no_of_trucks_weight = 0
    remaining_trucks_weight = 0
    flag=0
    #output for get_sku_with_km_sku
    path = pd.ExcelFile("/home/aravind/Desktop/schedulerui/backend/output_from_km_dimension.xlsx")
    df = pd.read_excel(path)
    depo = list(df["DEPO"].unique())
    weight = []
    volume = []

    day = str(datelist[0])[-2:]
    if(int(day) >= 16):
        '''checking if selected dates is in L2 INDENT '''
        g_wt=df.groupby("DEPO")["L2 Gross weight"].sum()
        v_wt = df.groupby("DEPO")["L1 volume "].sum()
        print(g_wt,v_wt)
    else:
        '''checking if selected dates is in L1 INDENT '''
        g_wt=df.groupby("DEPO")["L1 Gross weight"].sum()
        v_wt = df.groupby("DEPO")["L1 volume "].sum()
        print(g_wt,v_wt)

       
    #volume
    for i in depo:
            print(i)
    #1st truck
            iter=0
            iter_flag=0

            #to get truck capacity
            while(iter_flag==0):
                if i==truck_pref[iter][0]:
                    truck_cap=truck_pref[iter][1]
                    iter_flag=1
                iter=iter+1

            #calculate no of truck max weight wise
            no_of_trucks_volume=int(v_wt.get(i)/truck_capacity[truck_cap][1])
           

            # calculate no of truck remaining weight wise
            remaining_trucks_volume_temp=v_wt.get(i)-(no_of_trucks_volume * truck_capacity[truck_cap][1])
            
    #2nd truck
            if i == truck_pref[iter][0]:
                truck_cap = truck_pref[iter][1]
                remaining_trucks_volume = remaining_trucks_volume_temp / truck_capacity[truck_cap][1]
                rem_temp=v_wt.get(i)-(remaining_trucks_volume * truck_capacity[truck_cap][1])
                if rem_temp>0:
                    remaining_trucks_volume = remaining_trucks_volume + 1

    #case where 2nd truck option unavailable but still more sku to transport
            else:
                if remaining_trucks_volume_temp>0:
                    no_of_trucks_volume = no_of_trucks_volume + 1
            print(math.ceil(no_of_trucks_volume))
            volume.append([i,math.ceil(no_of_trucks_volume)])



    #weight
    for i in depo:
            print(i)
    #1st truck
            iter=0
            iter_flag=0

            #to get truck capacity
            while(iter_flag==0):
                if i==truck_pref[iter][0]:
                    truck_cap=truck_pref[iter][1]
                    iter_flag=1
                iter=iter+1

            #calculate no of truck max weight wise
            no_of_trucks_weight=int(g_wt.get(i)/truck_capacity[truck_cap][0])
           

            # calculate no of truck remaining weight wise
            remaining_trucks_weight_temp=g_wt.get(i)-(no_of_trucks_weight * truck_capacity[truck_cap][0])
            
    #2nd truck
            if i == truck_pref[iter][0]:
                truck_cap = truck_pref[iter][1]
                remaining_trucks_weight = remaining_trucks_weight_temp / truck_capacity[truck_cap][0]
                rem_temp=g_wt.get(i)-(remaining_trucks_weight * truck_capacity[truck_cap][0])
                if rem_temp>0:
                    remaining_trucks_weight = remaining_trucks_weight + 1

    #case where 2nd truck option unavailable but still more sku to transport
            else:
                if remaining_trucks_weight_temp>0:
                    no_of_trucks_weight = no_of_trucks_weight + 1
            print(math.ceil(no_of_trucks_weight))
            weight.append([i,math.ceil(no_of_trucks_weight)])
    #print(weight,volume)
    return [weight,volume]




a=tenative([15])



def volume_or_weight_map(wevol):
    weight = wevol[0]
    volume = wevol[1]
    true_list = []
    for i in range(len(volume)):
        if(volume[i][1]>weight[i][1]):
            temp = volume[i].append("volume")
            true_list.append(volume[i])
            
        else:
            temp = weight[i].append("weight")
            true_list.append(weight[i])
    print(true_list)



volume_or_weight_map(a)
