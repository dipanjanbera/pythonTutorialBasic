#take a word / sentence  from user and find no of occurence of a user given charecter in that word/sentence
str = raw_input("Enter any word or sentence ")
strToFound = raw_input("Enter a char ")
strToBuild = ""
print("\n")
count = 0;
for n in range(0,len(str)):
    ch = str[n].lower()
    if(ch==strToFound.lower()):
        count=count+1
print (count)
