std_info = {
    "Name" : "Kasidit",
    "Surname" : "Boonchai",
    "Student_id" : "64100738",
    "Age" : 19,
    "GPA" : 3.77
}

std_address = {
    "no." : "601/187",
    "moo" : "10",
    "tumbol" : "mueng",
    "amphor" : "Pakphanang",
    "jungwat" : "NST",
    "post_id" : "80000"
}

std_data = {
    "std_info" : std_info,
    "std_address" : std_address
}

for x,y in std_data.items():
    print(x,y)