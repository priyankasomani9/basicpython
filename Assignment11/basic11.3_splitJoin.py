# Python program to split a string and join it.

def split_string(string):
    splitString = string.split(' ')
    return splitString
def join_string(splitString):
    string = '-'.join(splitString)
    return string

if __name__ == '__main__':
    string = input("enter your string")
    splitedstring = split_string(string)
    print(splitedstring)

    newString = join_string(splitedstring)
    print(newString)
