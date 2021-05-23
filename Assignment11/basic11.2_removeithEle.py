# Python3 program for removing i-th indexed character from a string
def remove(string, i):
    a = string[: i]
    b = string[i + 1: ]
    return a + b
#way2
def remove1(string,i):
    for j in range(len(string)):
        if j == i:
            string = string.replace(string[i], "", 1)
    return string

if __name__ == '__main__':
    string = input("enter your string")
    i = int(input("enter index of a character which you want to remove-"))
    print(remove(string, i))
    print(remove1(string,i+1))
