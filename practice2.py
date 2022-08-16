x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#random number
import random

print(random.randrange(1,10))

q = "Hello, World!"
print(q[0])    #get a character from the string

for t in "Jeffrey":
    print(t)   #loop through the characters in a string

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")    #check if a phrase or char is present in the string
print(txt[2:5])      #get the characters from index 2 to index 4
print(txt[2:])       #get the characters from position 2, and all the way to the end
print(txt[:12])      #get the characters from the start to position 5
print(txt[-15:-4])
print(txt.upper())   #uppercase
print(txt.lower())   #lowercase
print(txt.strip())   #remove whitespace
print(txt.replace("t", "J"))  #replace a string with another string
print(q.split(","))  #returns a list where the text between the specified separator becomes the list items.

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))   #combining string and integer with format method

#escape characters
text = "We are the so-called \"Vikings\" from the north"    #double quote
text1 = 'It\'s alright'                             #single quote
text2 = "This will insert one \\ (backslash)"       #backslash
text3 = "Hello\nworld"                              #new line
text4 = "Hello\tworld"                              #tab
print(text)
print(text1)
print(text2)
print(text3)
print(text4)

