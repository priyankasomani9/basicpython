list1 = [[1, 2], [3, 4], [5, 6]]
list2 = [[3, 4], [5, 7], [1, 2]]
print("The original list 1 : " + str(list1))
print("The original list 2 : " + str(list2))
res_list = []
for i in list1:
    if i not in list2:
        res_list.append(i)
for i in list2:
    if i not in list1:
        res_list.append(i)
print("The uncommon of two lists is : " + str(res_list))
