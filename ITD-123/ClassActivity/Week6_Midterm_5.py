fee = 3500
regis_fee = 0
lec_credit = int(input("Input Lecture Credit : "))
lab_credit =  int(input("Input Lab Credit : "))
regis_fee = (lec_credit * 1000)+(lec_credit * 750) + fee
if regis_fee <= 5000:
    regis_fee = 5000
    print("Register Fee =",regis_fee)
elif regis_fee > 5000 and regis_fee <= 15000:
    print("Register Fee =",regis_fee)
elif regis_fee > 15000:
    regis_fee = 15000
    print("Register Fee =",regis_fee)