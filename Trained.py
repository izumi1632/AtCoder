def solve():
    N = int(input())
    a = [int(input()) for i in range(1, N + 1)]
    # ループしたら終わる
    l = []
    s = a[0]
    l = [0] * N
    c = 1
    l[0]=True
    while(True):
        l[s - 1] = True
        if s == 2:
            print(c)
            return True
        s = a[s - 1]
        if l[s - 1] == True:
            print(-1)
            return False
        c += 1
solve()


