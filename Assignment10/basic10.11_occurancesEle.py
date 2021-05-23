# Python code to count the number of occurrences
from collections import Counter
def countX(lst, x):
	count = 0
	for ele in lst:
		if (ele == x):
			count = count + 1
	return count

def count1(lst,x):
    return lst.count(x)
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x)))
print('{} has occurred {} times'.format(x, count1(lst, x)))
print('{} has occurred {} times'.format(x, Counter(lst)))


