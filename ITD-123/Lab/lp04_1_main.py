from datetime import date, datetime
now  = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Kasidit_Boonchai"
std_id = "64100738"
lab = "LP04-1"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-------------------------------------------")


#import function definition
import function_def as fn
fn.calculate_circle_area(5)
fn.calculate_circle_area(8)

fn.calculate_circumference(9)
fn.calculate_circumference(4)

fn.calculate_retangle_area(3,5)
fn.calculate_retangle_area(3,9)

fn.calculate_triangle_area(2,5)
fn.calculate_triangle_area(5,9)