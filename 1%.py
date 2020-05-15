import math
X = int(input())
c = 100
s = 0
while X > c:
  c = math.floor(c * 1.01)
  s += 1
print(s)

