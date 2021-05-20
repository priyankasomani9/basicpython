number=int(input("Enter any number"))
def factorial(number):
    if number<0:
        print("The number is invalid")
    else:
        if number ==0:
            return 1
        return number*factorial(number-1)
print(factorial(number))