str = raw_input("Enter a word you want ")
print ("Original Text: ",str)
reverseStr = ""
for n in range(len(str)-1,-1,-1):
    reverseStr+= str[n]
print ("Reversed Text: ",reverseStr)
