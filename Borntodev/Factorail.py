#example 01
'''num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Negative Number")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        print(factorial,"x",i)
        factorial = factorial*i
        print("sum =",factorial)
    print("Factorial of",num,"is",factorial)
'''
#example 02 Use recursive
def fact(n):
    return 1 if(n==1 or n==2)else n*fact(n-1)
print(fact(2))

#source : https://www.javatpoint.com/pyhton-factorial-number#:~:text=is%22%2C%20f)-,%23%20Python%20program%20to%20find%20%23%20factorial%20of%20given%20number%20import%20math,Factorial%20of%206%20is%20720