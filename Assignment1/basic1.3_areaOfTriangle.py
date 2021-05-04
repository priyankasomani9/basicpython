lengthOfFirstSide=float(input("enter the length of first side="))
lengthOfSecondSide=float(input("Enter the length of second side="))
lengthOfThirdSide=float(input("Enter the length of Third side="))
semiPerimeter=(lengthOfSecondSide+lengthOfSecondSide+lengthOfThirdSide)/2
areaOfTriangle = (semiPerimeter*(semiPerimeter-lengthOfFirstSide)*(semiPerimeter-lengthOfSecondSide)*(semiPerimeter-lengthOfThirdSide)) ** 0.5
print('The area of the triangle is %0.2f' %areaOfTriangle)

