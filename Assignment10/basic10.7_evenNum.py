#wap to print evem number from list
list=[]
evenlist=[]
n=int(input("how many number you want in a list:"))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
    if ele%2==0:
        evenlist.append(ele)
print(list)
print(evenlist)

