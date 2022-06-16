import numpy as np
def Passenger_Type ():
    print("MRT blue line ticket machine")
    print("Press 1 for Adult ticket\nPress 2 for Elder/Child ticket\nPress 3 for Student ticket")
    p_type = int(input(": "))
    p_station = int(input("Input select station (0-18) : "))
    if p_type > 3 or p_station > 18:
        print("\n##### Error : Invalid Number #####")
        Passenger_Type()
    return p_type,p_station

def Rate (p_type,p_station):
    adult = np.array([16,19,21,23,26,28,30,33,35,37,40,42])
    child = np.array([8,10,11,12,13,14,15,17,18,19,20,21])
    student = np.array([14,17,19,21,23,25,27,30,32,33,36,38])
    #! Adult ############################################
    if p_type == 1:
        if p_station <= 1:
            total = adult[0]
        elif p_station >= 12 and p_station <= 18 :
            total = adult[11]
        else:
            total = adult[p_station-1]
    #! Child ############################################
    elif p_type == 2:
        if p_station <= 1:
            total = child[0]
        elif p_station >= 12 and p_station <= 18 :
            total = child[11]
        else:
            total = child[p_station-1]
        #! Student ############################################
    elif p_type == 3:
        if p_station <= 1:
            total = student[0]
        elif p_station >= 12 and p_station <= 18 :
            total = student[11]
        else:
            total = student[p_station-1]
        #!#####################################################
    print("Fare =",total,"THB")
    return total

def Change (total):
    money_chk = False
    money = int(input("Please insert banknote/coin: "))
    while money_chk == False:
        if money < total:
            print("Require more cash....")
            money = int(input("Please insert banknote/coin: "))
        elif money >= total:
            print("Change",money - total,"THB\nGet your ticket, Thanks you\n")
            return money - total








#!Test
'''
while x is True:
    p_type = input("Input Passenger Type : ")
    p_station = int(input("Input select station (0-18) : "))
    #! Adult ############################################
    if p_type == '1':
        if p_station <= 1:
            total = adult[0]
        elif p_station >= 12 :
            total = adult[11]
        else:
            total = adult[p_station-1]
    #! Child ############################################
    elif p_type == '2':
        if p_station <= 1:
            total = child[0]
        elif p_station >= 12 :
            total = child[11]
        else:
            total = child[p_station-1]
    #! Student ############################################
    elif p_type == '3':
        if p_station <= 1:
            total = student[0]
        elif p_station >= 12 :
            total = student[11]
        else:
            total = student[p_station-1]
    #!#####################################################
    print("Fare =",total)

    # Change Part
    money = int(input("Please insert banknote/coin: "))
    money_chk = False
    #Loop
    while money_chk == False:
        if money < total:
            print("Require more cash....")
            money = int(input("Please insert banknote/coin: "))
        elif money >= total:
            money_chk = True
    print("Change",money - total,"\nGet your ticket, Thanks you")
'''

#!
'''
def Rate (p_type,p_station):
    price = np.array([[16,19,21,23,26,28,30,33,35,37,40,42],
                     [8,10,11,12,13,14,15,17,18,19,20,21],
                     [14,17,19,21,23,25,27,30,32,33,36,38]])
    #! Adult ############################################
    if p_type == 1:
        if p_station <= 1:
            total = price[0,0]
        elif p_station >= 12 and p_station <= 18 :
            total = price[0,11] 
        else:
            total = price[0,p_station-1]
    #! Child ############################################
    elif p_type == 2:
        if p_station <= 1:
            total = price[1,0]
        elif p_station >= 12 and p_station <= 18 :
            total = price[1,11]
        else:
            total = price[1,p_station-1]
        #! Student ############################################
    elif p_type == 3:
        if p_station <= 1:
            total = price[2,0]
        elif p_station >= 12 and p_station <= 18 :
            total = price[2,11]
        else:
            total = price[2,p_station-1]
        #!#####################################################
    print("Fare =",total)
    return total
'''