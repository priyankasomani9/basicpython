test_dict = {"Gfg" : 5, "is" : 3, "best" : 10}
print("The original dictionary is : " + str(test_dict))
updict = {"pre1" : 4, "pre2" : 8}
updict.update(test_dict)
print("The required dictionary : " + str(updict))
#way2
res1 = {**updict, **test_dict}
print("The required dictionary : " + str(res1))

