thislist = ["apple", "banana", 34 , "cherry", 12, True, "apple", 23+45j,"cherry"]
print(thislist)
thislist.append("ddd")
print(thislist)
thislist.insert(2,"qqqq")
print(thislist)
thislist.remove("cherry")
print(thislist)
print(thislist.index("cherry"))
print ("Size of List : ",len(thislist))

#ordered
#changable
#allow duplicate


#SeT
thisSet = {"apple", "banana", 34 , "cherry", 12, True, "apple", 23+45j,"cherry"}
print(thisSet)
thisSet.add("india")
print(thisSet)
thisSet.remove("banana")
print(thisSet)


#Tuple
thisTuple = ("apple", "banana", 34 , "cherry", 12, True, "apple", 23+45j,"cherry")
print(thisTuple)
print(thisTuple.index("cherry"))
print ("Size of Tuple: ",len(thisTuple))


#ordered
#NDuplicate values are allows
#Un-changable

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
},{
"brand": "TATA",
  "model": "Tiago",
  "year": 2020,
    "year": 2025
},{
    "Name":"ram",
    "roll":12,
    "class":3
}

print(thisdict)
#to access first record
print(thisdict[1])
#to print a specific value of a record
print(thisdict[2].get("model"))
#to print size of a dict
print (len(thisdict))

Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks', 3:'QQQQQ'})
print("\nDictionary with the use of dict(): ")
print(Dict)
