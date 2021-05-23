# Python program to find all string which are greater than given length k
def string_k(k, str):
    string = []
    text = str.split(" ")
    for x in text:
        if len(x) > k:
            string.append(x)
    return string
k = int(input("enter the value of k:"))
str = input("enter any string")
print(string_k(k, str))
