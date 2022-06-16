import json
from datetime import date, datetime
now  = datetime.now()
print("-------------------------------------------")
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Kasidit_Boonchai"
std_id = "64100738"
lab = "Lab 6"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-------------------------------------------")

locationlist = ["1. Bangkok",
"2. Kanchanaburi",
"3. Chanthaburi ",
"4. Chachoengsao",
"5. Chumphon",
"6. Chonburi",
"7. Trat ",
"8. Tak ",
"9. Nakhon Nayok " ,
"10. Nakhon Pathom ",
"11. Nonthaburi ",
"12. Pathum Thani",
"13. Prachuap Khiri ",
"14. Prachinburi ",
"15. Phra Nakhon Si Ayutthaya",
"16. Phetchaburi ",
"17. Ratchaburi ",
"18. Ranong ",
"19. Rayong ",
"20. Lopburi ",
"21. Singburi ",
"22. Samut Prakan  ",
"23. Samut Songkhram",
"24. Samut Sakhon",
"25. Suphanburi ",
"26. Sa Kaeo",
"27. Saraburi ",
"28. Ang Thong",
"0. Others"]

person_dict = {
    "fname": "",
    "lname": "",
    "age": 0,
    "body_temp": "",
    "location": "",
    "risk": False,
    "covid": False
}

person_dict.update({"fname":input("Enter first name: ")})
person_dict.update({"lname":input("Enter last name: ")})
person_dict.update({"age":int(input("Enter age: "))})
person_dict.update({"body_temp":int(input("Enter body temperature: "))})
for x in range (len(locationlist)) :
    print(locationlist[x])
person_dict.update({"location":int(input("Enter location number: "))})

if person_dict.get("location") <= 28 and person_dict.get("location") != 0:
    person_dict.update({"risk":True})
    if person_dict.get("body_temp") > 37.5:
        person_dict.update({"covid":True})

print(json.dumps(person_dict))