print("School of Informatics")
# Method 1 
iPhonePrice = 30000
gpax = 4.00
TextA = "iPhonePrice is {:,} Bath "
TextB =  "gpax is {:.2f}"
print(TextA.format(iPhonePrice))
print(TextB.format(gpax))
print("-----------------------------------")

# Method 2
std_name = "Kasidit Boonchai"
std_id = "64100738"
std_txt = "My name is {} and my student id is {}"
print(std_txt.format(std_name, std_id))
print("-----------------------------------")

# Method 3 
university_name = input()
faculty_name = input()
txt = "University name is {0} faculty name is {1}"
print(txt.format(university_name, faculty_name))