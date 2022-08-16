#dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
print(thisdict)

x = thisdict.get("model")
print(x)

#add a new item to the original dictionary

x = thisdict.keys()
y = thisdict.values()
z = thisdict.items()

print(x) #before the change
print(y)
print(z)

thisdict["color"] = "white"         #adding items

print(x) #after the change
print(y)
print(z)

#update dictionary
thisdict.update({"year": 2020})       #can also be used to add items
print(thisdict)

#remove items
thisdict.pop("model")
print(thisdict)

del thisdict["year"]
print(thisdict)

#loop through a dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
    print(x)                        #print all values

for x, y in thisdict.items():
  print(x, ":", y)                  #print all items

#copy a dictionary
mydict = dict(thisdict)
print(mydict)

#nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)



