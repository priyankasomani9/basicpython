punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
str = input("Enter a string: ")

no_punct = ""
for char in str:
   if char not in punctuations:
       no_punct = no_punct + char

print(no_punct)
