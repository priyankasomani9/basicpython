# Python program to check if a string is binary or not.
def check(string):
    p = set(string)
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        print("Yes")
    else:
        print("No")
if __name__ == "__main__":
    string = "101010000111"
    string1= "101010000112"
    check(string)
#way2
t = '01'
count=0
for char in string1:
    if char not in t:
        count=1
        break
    else:
        pass
if count:
    print("no")
else:
    print("yes")