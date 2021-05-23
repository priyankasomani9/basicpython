def returnSum(myDict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]

    return sum
dict = {'a': 500, 'b': 500, 'c': 500}
print("Sum :", returnSum(dict))
