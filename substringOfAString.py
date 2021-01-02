# Find substring of a word
str = raw_input("Enter any word ")
startPos = int(raw_input("Enter Starting Position : "))
endPos = int(raw_input("Enter End Position : "))
if startPos <= 1:
    startPos = 1
if endPos>=len(str):
    endPos = len(str)
if startPos<=endPos:
    strToBuild = ""
    for n in range(startPos-1,endPos):
        strToBuild+=str[n]
    print strToBuild
else:
    print "Incorrect Inputs"
