N,x = map(int,input().split())
a = sorted(map(int,input().split()),reverse=False)
ans = 0

if x > sum(a):
    print(N - 1)

else:
    for i in a:
        x -= i
        if x >= 0:
            ans += 1
    print(ans)