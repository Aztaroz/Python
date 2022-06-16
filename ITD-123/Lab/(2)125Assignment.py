chk = input("Press 'B' to convert binary to decimal\nPress 'O' to convert Octal to decimal\n") 
while chk == 'B' or chk == 'O':
    #! Input Part
    ############################################################                                         
    position = int(input("Input Position : "))                                                                      
    num = []
    for x in range(position):
        num.append(int(input("Input Number : ")))
    ############################################################
    b10 = 0
    element = len(num)
    print("Num in List is :",num,"\n::::::::::::::::::::::::::::::::::::")
    ############################################################
    #!Base 2 >> 10
    ############################################################
    if chk == 'B':
        for i in num:
            print("Element is :",element)
            position -= 1
            print("b2 is",i,"*","2 ^",position)
            if element != 1:
                multiply = int(i * 2**position)
                b10 = multiply + b10
            elif element == 1:
                b10 += i
            element -= 1
    ############################################################
    #!Base 8 >> 10
    ############################################################
    elif chk == 'O':
        for i in num:
            print("Element is :",element)
            position -= 1
            print("num is",i,"*","8 ^",position)
            if element != 1:
                multiply = int(i * 8**position)
                b10 = multiply + b10
            elif element == 1:
                b10 += i
            element -= 1
    ############################################################
    else :
        break
    print("multiply is",multiply,"+",b10,"sum\n::::::::::::::::::::::::::::::::::::")
    print("Base 10 is :",b10,"\n::::::::::::::::::::::::::::::::::::")
    chk = input("Press 'B' to convert binary to decimal\nPress 'O' to convert Octal to decimal\n")   
print("End process")




'''
Convert_Binary/Octal_to_Decimal
    GET chk
    DOWHILE chk = 'B' or chk = 'O'
        GET position
        SET num = [] #! ????
        DO x = 0 to position
            GET num[x]
        ENDDO
        SET base10 = 0
        SET element = num_element
        IF chk = 'B' THEN
            DO i = 0 to num
                position = position - 1
                IF element != 1 THEN
                    multiply = i * 2**position
                    base10 = multiply + base10
                ELSE IF element = 1 THEN
                    base10 = base10 + i
                ENDIF
                element = element - 1
            ENDDO
        ELSE IF chk = 'O' THEN
            DO i = 0 to num
                position = position - 1
                IF element != 1 THEN
                    multiply = i * 8**position
                    base10 = multiply + base10
                ELSE IF element = 1 THEN
                    base10 = base10 + i
                ENDIF
                element = element - 1
            ENDDO
        ENDIF
        DISPLAY base10
    ENDDO
    DISPLAY "End Process"
END
'''