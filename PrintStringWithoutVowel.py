str = raw_input("Enter any word or sentence ")
strToBuild = ""
print("\n")
count = 0;
for n in range(0,len(str)):
   if(n<len(str)):
       ch = str[n].lower()
       if (ch != 'a' and ch != 'e' and ch != 'i' and ch != 'o' and ch != 'u'):
           strToBuild = strToBuild + str[n]

print (strToBuild)
