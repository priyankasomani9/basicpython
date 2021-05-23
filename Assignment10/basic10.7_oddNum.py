#wap to print evem number from list
list=[]
oddlist=[]
n=int(input("how many number you want in a list:"))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
    if ele%2==1:
        oddlist.append(ele)
print(list)
print(oddlist)

