#You can use double or single quotes:

x = "my Name is AMARTYA."
y = "I am {} years old."
print("To make all letter as lower case :", x.lower()) 
print("To make all letter as uper case :", x.upper()) 
print("To calculate length of string :", len(x)) 
print("To split a string based on some parameter , here it is space:",x.split(" ")) 
print("Search a word within a sentence ","AMARTYA" in x) 
print("Search a word within a sentence ","India" not in x) 
print("To join 2 string variables: ",x+y) 
print("To add a extra space between 2 string variables : ",x+' '+y) 
print("To format a String variable : ",x+y.format(40)) 
print("To replace a string variable :",x.replace("AMARTYA" , "Ram")) 
print("To replace a string variable :",x.replace("AM" , "R")) 
print("To find a word or letter in a String :",x.rfind("Name")) 
print("To make First letter as uper case and others as lower case :",x.capitalize()) 
print("Make the first letter in each word upper case :",x.title()) 
print("Return the number of times a value appears in the string:" ,x.count("A")) 
print("To find a word or letter in a String :",x.find("Name")) 
print("To find a word or letter in a String IF not found :",x.find("Nameer")) 
print("To find a word or letter in a String by index:",x.index("Name")) 
print("To find a word or letter in a String IF not found then it shows error :",x.index("Name")) 
print("To check a string is in upper case or not  :",x.isupper()) 
print("To check a string is in lower case or not  :",x.islower()) 
z = "2345" 
print("To check a string is a digit or not  :",z.isdigit()) 
a = "Company12"
print("To check a string is a alpha-numeric or not  :",a.isalnum()) 
print("Check if all the characters in the text are letters: ",a.isalpha())
b = "     banana     " 
print("Remove spaces at the beginning and at the end of the string : ", "of all fruits", b.strip(), "is my favorite") 
print("Remove spaces at the beginning of the string : ", "of all fruits", b.lstrip(), "is my favorite") 
print("Remove spaces  at the ending  of the string : ", "of all fruits", b.rstrip(), "is my favorite")


