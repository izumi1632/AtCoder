N, M = map(int , input().split())

a = [0] * M
b = [0] * M

count = [0] * N

for i in range(0, M):
    a[i], b[i] = map(int, input().split())
    count[a[i] - 1]+=1
    count[b[i] - 1]+=1

for i in range(N):
    print(count[i])


