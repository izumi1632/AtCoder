import math
a,b,x = map(int,input().split())
#print(sum([1 for i in range(a,b+1) if i % x == 0]))
print(b // x - (a - 1) // x)
