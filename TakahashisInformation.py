def solve():
    c = [list(map(int, input().split())) for _ in range(3)]

    a = [0] * 3
    # a[0]を０とすると全部決まる？
    a[0] = 0
    b = c[0]
    a[1] = c[1][0] - b[0]
    a[2] = c[2][0] - b[0]

    for i in range(3):
        for j in range(3):
            if c[i][j] != a[i] + b[j]:
                print('No')
                return
    print('Yes')

def main():
    solve()

if __name__ == '__main__':
    main()