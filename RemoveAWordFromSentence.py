str = raw_input("Enter any word or sentence ")
strToRemove = raw_input("enter any word to remove ")
words = str.split(" ")
words.remove(strToRemove)
strRemoved=""
print (strRemoved+" ".join(words))
