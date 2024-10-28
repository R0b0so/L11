print("Half pyramid")
a = int(input("How many rows?"))
for i in range(a):
 for j in range(i+1):
  print("* ", end="")
 print()