def car(n):
    if(n == 1):
        return 1
    else:
        return car(n-1)+1
print(car(10))