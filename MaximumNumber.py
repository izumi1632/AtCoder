input()
min = 10**9
max = 0
list = list(map(int,input().split()))
for i in list:
    if min > i:
        min = i
    if max < i:
        max = i
print(max - min)