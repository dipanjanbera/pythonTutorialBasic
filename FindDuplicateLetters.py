# Find duplicate letters from a word
str = raw_input("Enter any word ")
a = list()
duplicateLetters = list()
for n in range(0,len(str)-1):
    if str[n]  in a:
        duplicateLetters.append(str[n])
    else:
        a.append(str[n])
print duplicateLetters


