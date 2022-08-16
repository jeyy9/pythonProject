#if else using Elif

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
    print("a is greater than b")

#if else short statement
c = 2
d = 8
print("A") if a > b else print("B")

#if else multiple statements
e = 330
f = 330
print("A") if a > b else print("=") if a == b else print("B")

#while loops
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#while else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#for loops continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#for else
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
  #if the loop breaks, the else block is not executed

#nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)