def calculateLength(number):
    length=0
    while(number!=0):
        length=length+1
        number=number//10
    return length
def sumDigit(number):
    sum=0
    lengthValue=calculateLength(number)
    temp=number
    while(number>0):
        remaining=number%10
        sum=sum+ int(remaining**lengthValue)
        number=number//10
        lengthValue=lengthValue-1
    return sum

for number in range(1,101):
    sum=sumDigit(number)

    if sum==number:
        print(number)

