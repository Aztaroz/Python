from datetime import date, datetime
now  = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Kasidit_Boonchai"
std_id = "64100738"
lab = "LP03-2-1"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-------------------------------------------")

print("Children record list...")
child_num = int(input("How many children(s): "))
i = 0
weight = []
height = []
overall_weight = 0
overall_height = 0
print("---------------------------------------")
if child_num <= 20 and child_num >= 1:
    while i < child_num:
        print("Children #{}".format(i+1))
        weight.append(float(input("Enter weight(kg): ")))
        height.append(float(input("Enter height(M): ")))
        print("---------------------------------------")
        i+=1
    for i in range(child_num):
        overall_weight = weight[i] + overall_weight
        overall_height = height[i] + overall_height
    print("Average of weight = {:.2f} kg".format(overall_weight/child_num))
    print("Average of height = {:.2f} M".format(overall_height/child_num))
    print("---------------------------------------")
else:
    print("Error please input less or equal 20")
    print("---------------------------------------")