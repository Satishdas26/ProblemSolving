def multiplesum(n):
    sum = 0
    for i in range(n):
        if(i%3==0 or i%5==0):
            sum=sum+i
    return sum

n = int(input("Enter a Natual Number:-"))
print("Sum:-", multiplesum(n))    