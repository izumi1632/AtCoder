N = int(input())
C = {}
#A = [int(input()) for x in range(N)]

for i in range(N):
    a = int(input())
    if a in C:
        C[a] += 1
    else:
        C[a] = 1

print(len([1 for i in C.values() if i % 2 == 1]))