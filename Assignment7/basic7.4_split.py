arr=[]
#take array element from user
n=int(input("how many number of element you want in array="))
for i in range(0,n):
    element=int(input())
    arr.append(element)
print(arr)

def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n - 1):
            arr[j] = arr[j + 1]

        arr[n - 1] = x
n = len(arr)
position = 2

splitArr(arr, n, position)

for i in range(0, n):
    print(arr[i], end=' ')
