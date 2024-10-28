print("Half pyramid")
a = int(input("How many rows?"))
b = 1
for i in range(a):
 for j in range(i+1):
  print(b, end=" ")
  b = b + 1
 print()