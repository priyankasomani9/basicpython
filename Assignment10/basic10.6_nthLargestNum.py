arr=[]
n=int(input("how many number of element you want in list"))
for i in range(0,n):
    n= int(input())
    arr.append(n)
print(arr)
print("Given array:", arr)
arr.sort()
print("Sorted array:", arr)
nthelement=int(input("Enter which place element you want:"))
print("the nth largest element",arr[nthelement])
print("the nth largest element",arr[-nthelement:])
