def calculateLength(number):
    length=0
    while(number!=0):
        length=length+1
        number=number//10
    return length
number=int(input("Enter any number"))
numbercopy=number
remaining=sum=0
lengthValue=calculateLength(number)
temp=number
while(number>0):
    remaining=number%10
    sum=sum+ int(remaining**lengthValue)
    number=number//10
    lengthValue=lengthValue-1
if(sum == numbercopy):
    print(str(numbercopy) + " is a disarium number");
else:
    print(str(numbercopy) + " is not a disarium number");



