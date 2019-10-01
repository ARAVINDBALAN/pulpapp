import pandas as pd

#inputs are main data after stage one and no of days_remaining

truck_capacity = {160: [16000, 28560000], 145: [14500, 58540000], 90: [9000, 25870000], 65: [6500, 35000000]}
truck_pref=[["KL01",160],["KL01",90],["AP01",65],["AP03",65],["GO01",160],["KK01",160],["KK02",160],["KK02",145],["TN01",160],["TN02",90],["TN03",90],["MH01",65],["MH02",145],["MH04",160]]
depo=["KL01","AP01","AP03","GO01","KK01","KK02","TN01","TN02","TN03","MH01","MH02","MH04"]
depo_qt=[None]

def tenative():
    weight = 0
    volume = 0
    no_of_trucks_volume = 0
    remaining_trucks_volume = 0
    no_of_trucks_weight = 0
    remaining_trucks_weight = 0
    flag=0
    path = pd.ExcelFile(root[0] + "\\input\\Output.xlsx")
    df = pd.read_excel(path, "Sheet1")
    g_wt=df.groupby("DEPO")["GT"].sum()
    v_wt = df.groupby("DEPO")["VOL"].sum()
    g_wt=g_wt.set_index("DEPO")
    v_wt = v_wt.set_index("DEPO")

    #volume
    for i in depo:

    #1st truck
            iter=0
            iter_flag==0

            #to get truck capacity
            while(iter_flag==0):
                if i==truck_pref[iter][0]:
                    truck_cap=truck_pref[iter][1]
                    iter_flag=1
                iter=iter+1

            #calculate no of truck max vol wise
            no_of_trucks_volume=int(v_wt.iloc(i)/truck_capacity[truck_cap][1])

            # calculate no of truck remaining vol wise
            remaining_trucks_volume_temp=v_wt.iloc(i)-(no_of_trucks_volume * truck_capacity[truck_cap][1])

    #2nd truck
            if i == truck_pref[iter][0]:
                truck_cap = truck_pref[iter][1]
                remaining_trucks_volume = remaining_trucks_volume_temp / truck_capacity[truck_cap][1]
                rem_temp=v_wt.iloc(i)-(remaining_trucks_volume * truck_capacity[truck_cap][1])
                if rem_temp>0:
                    remaining_trucks_volume = remaining_trucks_volume + 1

    #case where 2nd truck option unavailable but still more sku to transport
            else:
                if remaining_trucks_volume_temp>0:
                    no_of_trucks_volume = no_of_trucks_volume + 1

    #weight
    for i in depo:

    #1st truck
            iter=0
            iter_flag==0

            #to get truck capacity
            while(iter_flag==0):
                if i==truck_pref[iter][0]:
                    truck_cap=truck_pref[iter][1]
                    iter_flag=1
                iter=iter+1

            #calculate no of truck max weight wise
            no_of_trucks_volume=int(v_wt.iloc(i)/truck_capacity[truck_cap][1])

            # calculate no of truck remaining weight wise
            remaining_trucks_volume_temp=v_wt.iloc(i)-(no_of_trucks_volume * truck_capacity[truck_cap][1])

    #2nd truck
            if i == truck_pref[iter][0]:
                truck_cap = truck_pref[iter][1]
                remaining_trucks_volume = remaining_trucks_volume_temp / truck_capacity[truck_cap][1]
                rem_temp=v_wt.iloc(i)-(remaining_trucks_volume * truck_capacity[truck_cap][1])
                if rem_temp>0:
                    remaining_trucks_volume = remaining_trucks_volume + 1

    #case where 2nd truck option unavailable but still more sku to transport
            else:
                if remaining_trucks_volume_temp>0:
                    no_of_trucks_volume = no_of_trucks_volume + 1











