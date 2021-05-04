#dis = (b**2) - (4 * a*c)
import cmath
a=1
b=2
c=3
dis = (b**2) - (4 * a*c)
root1 = (-b-cmath.sqrt(dis))/(2 * a)
root2 = (-b + cmath.sqrt(dis))/(2 * a)
print("the roots are {} {}".format(root1,root2))