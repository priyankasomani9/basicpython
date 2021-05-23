import re
def run(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (regex.search(string) == None):
        print("String is not having special character")
    else:
        print("String is having special character")
if __name__ == '__main__':
    string = input("Enter any string")
    run(string)
