N, A, B = map(int, input().split())

s = 0
for i in range(1, N + 1):
    tmp = 0
    for k in str(i):
        tmp += int(k)    
    if A <= tmp and tmp <= B:
        s += i
print(s)