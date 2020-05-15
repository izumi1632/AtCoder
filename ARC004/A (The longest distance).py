N = int(input())
XY = list([input().split() for i in range(N)])
maxDistance = 0
for xy in XY:
  x,y = map(int, xy)
  for xy2 in XY:
    x2,y2 = map(int, xy2)
    maxDistance = max(maxDistance, ((x2-x)**2 + (y2-y)**2)**0.5)
print(maxDistance)
