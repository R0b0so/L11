print("Triangle")
a = int(input("How many rows?"))
for i in range(1, a + 1):
  for j in range(1, (a-i)+1):
   print(" ", end="")
  for t in range(1, i+1):
   print("* ", end="")
  print()
 