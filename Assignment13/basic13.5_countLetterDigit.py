string=input("Enter a String:")
digit=letter=0
for i in string:
    if i.isdigit():
        digit=digit+1
    elif i.isalpha():
        letter=letter+1
    else:
        pass
print("count of digit is",digit)
print("count of letter is",letter)
