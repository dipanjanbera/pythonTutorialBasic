str = raw_input("Enter any sentence ")
words = str.split(" ")
d = dict()
# putting length of each words in Dictionary as key value pair , where key is word and value is length of the word
for word in words:
    d[word] = len(word)

# min function is used to get the key with min value
Keymax = min(d, key=d.get)
print(Keymax)


