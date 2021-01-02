#find no of vowel from a word or sentence
str = raw_input("Enter any word or sentence ")
print("\n")
count = 0;
for n in range(0,len(str)):
   ch = str[n].lower()
   if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
       count += 1
   #print (ch)
print ("Number of Vowel ",count)
print ("Number of Consonant  ",len(str)-count)
