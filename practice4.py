#tuple

#add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)             #remember to use comma, otherwise pyhton will decide it as an error
thistuple += y

print(thistuple)

#unpacking a tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#using a asterisk

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#set

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")                       #add one item to the set

print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)                    #add items from another set into the current set

print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()

print(x)                                    #removed item
print(thisset)                              #the set after removal

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)                     #returns a new set with all items from both sets

print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)                           #inserts the items in set2 into set1
print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)                    #keep only the duplicates

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)           #keep all but not the duplicates

print(x)
