number1=int(input("enter first number="))
number2=int(input("enter second number="))
def compute_lcm(number1, number2):
   if number1 > number2:
       greater = number1
   else:
       greater = number2
   while(True):
       if((greater % number1 == 0) and (greater % number2== 0)):
           lcm = greater
           break
       greater += 1

   return lcm


print("The L.C.M. is", compute_lcm(number1, number2))