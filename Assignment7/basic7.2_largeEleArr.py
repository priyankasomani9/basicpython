array=[]
#take array element from user
n=int(input("how many number of element you want in array="))
for i in range(0,n):
    element=int(input())
    array.append(element)
print(array)

#find and print max
print(max(array))
