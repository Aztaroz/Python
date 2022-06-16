from datetime import date, datetime
now  = datetime.now()
print("-------------------------------------------")
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Kasidit_Boonchai"
std_id = "64100738"
lab = "Lab Quiz 3"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-------------------------------------------")

import Lab_Quiz_3 as fn
call_input = int(input("Enter amount of calling(minute) : "))
data_input = float(input("Enter amount of data(GB) : "))
#Call Mobile Billing
net_amount = fn.mobile_biling(call_input,data_input)
print("Current Charge",net_amount)
#Call Discount
discount = fn.discount(net_amount)
print("Discount {:.2f}".format(discount))
#Print Excluded Vat
print("Charge excluded vat.",net_amount - discount,"THB")
#Call/Print VAT
print("Total Payment {:.2f}".format(fn.vatable(net_amount - discount)),"THB (vat.7% included)")