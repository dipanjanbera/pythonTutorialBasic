str = raw_input("Enter any word or sentence ")
words = str.split(" ")
d = dict()
for word in words:
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
for key in list(d.keys()):
    print(key, ":", d[key])
