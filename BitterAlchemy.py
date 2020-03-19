N ,X = map(int, input().split())
m = [int(input()) for _ in range(N)]
minW = 1000
c = 0

for i in m:
    X -= i
    if minW > i:
        minW = i
c += N

while X - minW >= 0:
    X -= minW
    c += 1

print(c)