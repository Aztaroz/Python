crn_time = int(input("Enter the time in hours: "))
alarm = int(input("Enter the alarm time in hours: "))
sum = (alarm - crn_time)%24
print("There is",sum,"hours left to alarm")