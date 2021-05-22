input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()
print('list: ', user_list)

for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])

# Calculating the sum of list elements
print("Sum = ", sum(user_list))

list1=[]
sum1=0
n=int(input("how many number of element you want in list"))
for i in range(0,n):
    n= int(input())
    list1.append(n)
print(list1)
print(sum(list1))