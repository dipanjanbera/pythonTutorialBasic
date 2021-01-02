#concat of number of strings
number = int(input("Enter No of string you want "))
str = ""
for n in range(0,number):
    strToTake = raw_input("Enter a string ")
    str+=strToTake+" ";
print str
