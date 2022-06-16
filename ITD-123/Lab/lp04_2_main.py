import lp04_2_utilityfunc as fn

from datetime import date, datetime
now  = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Kasidit_Boonchai"
std_id = "64100738"
lab = "LP03-1-2"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-------------------------------------------")

fn.validate_person_id("1234567890121")
fn.get_email()