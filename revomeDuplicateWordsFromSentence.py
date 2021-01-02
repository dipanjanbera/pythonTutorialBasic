# Remove duplicate words from a sectence 
str = raw_input("Enter any sentence ")
words = str.split(" ")
d = dict()
strToBuild = ""
for word in words:
    if word not in d:
        strToBuild += word + " "
        d[word] = 1
print("Final String with unique words : ",strToBuild)
