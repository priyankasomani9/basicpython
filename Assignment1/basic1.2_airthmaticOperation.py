number1=int(input("Enter first number"))
number2=int(input("enter second number"))
print("sum={}".format(number1+number2))
try:
    result =number1/number2
except ZeroDivisionError:
    result=0