def avg_recursive():
    print("------------------------")
    sum = 0
    num = []
    for i in range (0,3):
        num.append(int(input("Input 3 Number : ")))
    for i in num:
        sum = i + sum
        avg = sum / len(num)
    if avg > num[0] + num[1]:
        print("The End")
    else:
        avg_recursive()
    print("------------------------")
avg_recursive()