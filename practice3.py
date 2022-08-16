a = 200
b = 33

if b > a:
    print("b is greater than a")
else :
    print("b is not greater than a")

bool(None)
bool(0)
bool(())

#create functions that returns a boolean value
def myFunction() :
  return True

print(myFunction())

#execute code based on the Boolean answer of a function
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#check if an object is of a certain data type
r = 200
print(isinstance(r, int))

a += 25
print(a)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)           # returns True because z is the same object as x
print(x is y)           # returns False because x is not the same object as y, even if they have the same content
print(x == y)           # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y






