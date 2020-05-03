import sys
X = int(input())
for i in range(-120,120):
  for j in range(-120,120):
    if i**5 - j **5 == X:
      print(str(i)+" "+str(j))
      sys.exit()