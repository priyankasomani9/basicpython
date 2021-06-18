wordlist=[]
string=input()
splitOfString=string.split(' ')
print(splitOfString)
for i in splitOfString:
    if i not in wordlist:
        wordlist.append(i)
    else:
        continue
wordlist.sort()
print(wordlist)
print((' ').join(wordlist))
