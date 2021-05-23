# Python code to merge dict
#way1
def Merge(dict1, dict2):
    return (dict2.update(dict1))
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
print(Merge(dict1, dict2))
print(dict2)
#way2
def Merge1(dict1,dict2):
    res={**dict1,**dict2}
    return  res
print(Merge1(dict1,dict2))
