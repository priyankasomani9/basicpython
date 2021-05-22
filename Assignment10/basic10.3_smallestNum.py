list1=[]
n=int(input("how many number of element you want in list"))
for i in range(0,n):
    n= int(input())
    list1.append(n)
print(list1)
list1.sort()
#print("Smallest element is:", *list1[:1])
print("Smallest element is:", min(list1))
