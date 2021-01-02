str = raw_input("Enter any sentence ")
words = str.split(" ")
d = dict()
# putting length of each words in Dictionary as key value pair , where key is word and value is length of the word
for word in words:
    d[word] = len(word)

# max function is used to get the key with max value
Keymax = max(d, key=d.get)
print(Keymax)
