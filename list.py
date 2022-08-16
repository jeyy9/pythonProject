thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist[1])      # print the second item of the list
print(thislist[2:5])    # return the third, fourth, and fifth item

thislist[1:3] = ["blackcurrant","watermelon"]
print(thislist)         # change the value of items within a specific range

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)         # add an item to the end of the list

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)         # append elements from another list to current list

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)              # loop through a list

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])    # loop through index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]    #looping using list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)                  #list comprehension

newlist1 = [x for x in range(10)]           #iterable
newlist2 = [x for x in range(10) if x < 5]  #iterable with condition
print(newlist1)
print(newlist2)
newlist3 = [x.upper() for x in fruits]      #expression
newlist4 = ['hello' for x in fruits]        #set all values to hello
newlist5 = [x if x!= "banana" else "orange" for x in fruits]      #manipulate the outcome

thislist1= [100, 50, 62, 80, 23]
thislist1.sort()
print(thislist1)                            #sort ascending
thislist1.sort(reverse = True)
print(thislist1)                            #sort descending

thislist2 = ["banana", "Orange", "Kiwi", "cherry"]
thislist2.sort(key = str.lower)
print(thislist2)                            #sorting case-insensitive order
thislist2.reverse()
print(thislist2)                            #reverse the current order of the list

#copy list
mylist = thislist2.copy()
print(mylist)
mylist1 = list(thislist2)
print(mylist1)                #both methods are the same

#join list
list1 = thislist1 + thislist2
print(list1)                    #using + operator

for x in thislist2:
  thislist1.append(x)           #using append

print(thislist1)

thislist1.extend(thislist2)
print(thislist1)                #using extend














