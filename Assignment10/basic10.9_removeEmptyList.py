list = [5, 6, [], 3, [], [], 9]
print("The original list is : " + str(list))
res = [ele for ele in list if ele != []]
print ("List after empty list removal : " + str(res))


