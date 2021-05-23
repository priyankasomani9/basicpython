from itertools import chain

test_dict = {'gfg' : [5, 6, 7, 8],
			'is' : [10, 11, 7, 5],
			'best' : [6, 12, 10, 8],
			'for' : [1, 2, 5]}

print("The original dictionary is : " + str(test_dict))
res = list(sorted({ele for val in test_dict.values() for ele in val}))
print("The unique values list is : " + str(res))
#way2
res1 = list(sorted(set(chain(*test_dict.values()))))
print("The unique values list is : " + str(res1))
#way3
dict = {'511':'Vishnu','512':'Vishnu','513':'Ram','514':'Ram','515':'sita'}
list=[]
for val in dict.values():
    if val in list:
        continue
    else:
        list.append(val)
print(list)

