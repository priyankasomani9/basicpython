list=[]
n=int(input("how many element you want in list"))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)
result=[]
for i in list:
    if i not in result:
        result.append(i)
    else:
        print(i,end=' ')