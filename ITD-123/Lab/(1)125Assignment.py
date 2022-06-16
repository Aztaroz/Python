#วนซ้ำรับข้อมูล

letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rot13 = []                                  
cc = []
text = []
length = int(input("Input Lenght : "))
for i in range (length):
    text.append(input("Input Text : "))
chk = input("Encrypt or Decrypt?\n")
if chk == "เข้ารหัส":
    for x in text:
        index = 0
        for y in letter:
            if x == y:  # Caesar Cipher
                ans = (index + 3) % 26
                print("Index :",index)
                cc.append(letter[ans])
            if x == y:  # ROT 13
                ans = (index + 13) % 26
                rot13.append(letter[ans])
            index +=1
    
elif chk == "ถอดรหัส":
    for x in text:
        index = 0
        for y in letter:
            if x == y:  # Caesar Cipher
                ans = (index - 3) % 26
                cc.append(letter[ans])
            if x == y:  # ROT 13
                ans = (index - 13) % 26
                rot13.append(letter[ans])
            index +=1
print("Caesar Cipher :",*cc,"\nROT 13 :",*rot13)



'''
Pseudocode
Decode_Encode_r13_CC
    SET letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    SET rot13 = []
    SET caesar_cipher = []
    SET text = []
    GET length
    DO i = 1 to length
        GET text[i]
    ENDDO
    GET chk
    IF chk = "เข้ารหัส" THEN
        DO x = 1 to length
                DO y = 1 to 26
                    IF text[x] = letter[y] THEN
                        ans = (y + 3) % 26
                        ADD letter[ans] to caesar_cipher
                        ans = (y + 13) % 26
                        ADD letter[ans] to rot13
                    ENDIF
                ENDDO
        ENDDO
    ELSE iF chk = "ถอดรหัส" THEN
       DO x = 1 to length
                DO y = 1 to 26
                    IF text[x] = letter[y] THEN
                        ans = (y - 3) % 26
                        ADD letter[ans] to caesar_cipher
                        ans = (y - 13) % 26
                        ADD letter[ans] to rot13
                    ENDIF
                ENDDO
        ENDDO
    ENDIF
    DISPLAY caesar_cipher, rot13
END



a = [ 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' ]
n = "HELLO"
i = 0
j = 0
b = []

for i in range(len(n)):
    for j in range(len(a)):
        if n[i] == a[j]:
            if j <= 12:
                b.append(a[j+13])
            else:
                b.append(a[j-13])
for i in b:
    print(f"{i}",end='')
'''