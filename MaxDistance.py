import math
N = int(input())
xy = list()
for i in range(N):
    xy.append(list(map(int,input().split())))

maxD = 0.0
for i in xy:
    for k in xy:
        distance = math.sqrt((i[0]-k[0])**2 + (i[1]-k[1])**2)
        if distance > maxD:
            maxD = distance
print(maxD)
        
