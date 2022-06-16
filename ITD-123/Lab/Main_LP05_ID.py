import numpy as np
import LP05_ID as fn
from datetime import date, datetime
now  = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Kasidit_Boonchai"
std_id = "64100738"
lab = "LP05"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-------------------------------------------")

type = fn.Passenger_Type()
price = fn.Rate(*type)
fn.Change(price)