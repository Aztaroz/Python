'''print("Children record list...")
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
        gender = str(input("Enter Gender : "))
        weight.append(float(input("Enter weight(kg): ")))
        height.append(float(input("Enter height(M): ")))
        if weight[i] >= 2.7 and weight[i] <= 3.9 and height[i] >=46.8 and height[i] <= 53.1:        #0
            print("Children No.{} is qualified (For Children 0 Year 0 Month)".format(i+1))
        elif weight[i] >= 3.3 and weight[i] <= 4.7 and height[i] >= 49.4 and height[i] <= 56.2:     #1
            print("Children No.{} is qualified (For Children 0 Year 1 Month)".format(i+1))
        elif weight[i] >= 3.8 and weight[i] <= 5.5 and height[i] >= 52.0 and height[i] <= 59.1:     #2
            print("Children No.{} is qualified (For Children 0 Year 2 Month)".format(i+1))
        elif weight[i] >= 4.4 and weight[i] <= 6.4 and height[i] >= 54.4 and height[i] <= 61.9:     #3
            print("Children No.{} is qualified (For Children 0 Year 3 Month)".format(i+1))
        elif weight[i] >= 4.9 and weight[i] <= 7.1 and height[i] >= 56.8 and height[i] <= 64.6:     #4
            print("Children No.{} is qualified (For Children 0 Year 4 Month)".format(i+1))
        elif weight[i] >= 5.3 and weight[i] <= 7.8 and height[i] >= 58.9 and height[i] <= 67.1:     #5
            print("Children No.{} is qualified (For Children 0 Year 5 Month)".format(i+1))
        elif weight[i] >= 5.8 and weight[i] <= 8.4 and height[i] >= 60.9 and height[i] <= 69.2:     #6
            print("Children No.{} is qualified (For Children 0 Year 6 Month)".format(i+1))
        elif weight[i] >= 6.2 and weight[i] <= 9.0 and height[i] >= 62.6 and height[i] <= 71.3:     #7
            print("Children No.{} is qualified (For Children 0 Year 7 Month)".format(i+1))
        elif weight[i] >= 6.6 and weight[i] <= 9.5 and height[i] >= 64.2 and height[i] <= 73.2:     #8
            print("Children No.{} is qualified (For Children 0 Year 8 Month)".format(i+1))
        elif weight[i] >= 6.9 and weight[i] <= 9.9 and height[i] >= 65.5 and height[i] <= 75.0:     #9
            print("Children No.{} is qualified (For Children 0 Year 9 Month)".format(i+1))
        elif weight[i] >= 7.2 and weight[i] <= 10.3 and height[i] >= 66.7 and height[i] <= 76.7:     #10
            print("Children No.{} is qualified (For Children 0 Year 10 Month)".format(i+1))
        elif weight[i] >= 7.5 and weight[i] <= 10.6 and height[i] >= 67.7 and height[i] <= 78.2:     #11
            print("Children No.{} is qualified (For Children 0 Year 11 Month)".format(i+1))
        elif weight[i] >= 7.7 and weight[i] <= 11.0 and height[i] >= 68.8 and height[i] <= 79.7:     #1
            print("Children No.{} is qualified (For Children 0 Year 12 Month)".format(i+1))
        elif weight[i] >= 9.7 and weight[i] <= 14.4 and height[i] >= 80.8 and height[i] <= 91.5:     #2
            print("Children No.{} is qualified (For Children 1 Year 0 Month)".format(i+1))
        elif weight[i] >= 11.5 and weight[i] <= 17.2 and height[i] >= 88.1 and height[i] <= 100.8:     #3
            print("Children No.{} is qualified (For Children 2 Year 0 Month)".format(i+1))
        elif weight[i] >= 13.0 and weight[i] <= 19.9 and height[i] >= 95.0 and height[i] <= 108.2:     #4
            print("Children No.{} is qualified (For Children 3 Year 0 Month)".format(i+1))
        elif weight[i] >= 14.4 and weight[i] <= 22.6 and height[i] >= 101.1 and height[i] <= 115.1:     #1
            print("Children No.{} is qualified (For Children 4 Year 0 Month)".format(i+1))
        else:
            print("Children No.{} is not qualified")
        print("---------------------------------------")
        i+=1
    for i in range(child_num):
        overall_weight = weight[i] + overall_weight
        overall_height = height[i] + overall_height
    print("Average of weight = {:.2f}".format(overall_weight/child_num))
    print("Average of height = {:.2f}".format(overall_height/child_num))
    print("---------------------------------------")
   
else:
    print("Error please input less or equal 20")
    print("---------------------------------------") '''

'''
def Caesar_Nomal(text):
    Nomal = []
    for i in text:
        if 90 >= ord(i) >= 88:
            j = (ord(i) % 88) + 65
        elif 122 >= ord(i) >= 120:
            j = (ord(i) % 120) + 97
        else:
            j = ord(i) + 3
        Nomal.append(chr(j))
    return Report(Nomal)

def Nomal_Caesar(text):
    Nomal = []
    for i in text:
        if 67 >= ord(i) >= 65:
            j = (ord(i) % 65) + 88
        elif 99 >= ord(i) >= 97:
            j = (ord(i) % 97) + 120
        else:
            j = ord(i) - 3
        Nomal.append(chr(j))
    return Report(Nomal)

def Report(text):
    print(end="Result : ")
    for i in text:
        print(end="{}".format(i))
    return

A = input("Please : ")
print(end="Decrypt ")
Nomal_Caesar(A)
print(end="\nEncrypt ")
Caesar_Nomal(A)
'''

x = 0
y = {10,20}
print("success")