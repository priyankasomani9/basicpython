def checkHarshadNum(number):
    rem = sum = 0;
    n = number;
    while(number > 0):
        rem = number%10;
        sum = sum + rem;
        number = number//10;

    if(n%sum == 0):
        print(str(n) + " is a harshad number");
    else:
        print(str(n) + " is a not harshad number");
for i in range(1,101):
    checkHarshadNum(i)



