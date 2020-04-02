def solve():
    ABC = list(sorted(map(int, input().split())))

    A, B, C = ABC[0], ABC[1], ABC[2]

    a, amod = divmod((C-A),2)
    b, bmod = divmod((C-B),2)
    A += a * 2
    B += b * 2

    if C == A and C == B:
        return a + b
    elif C > A and C > B:
        return a + b + 1
    elif C > A and C == B:
        return a + b + 2
    elif C > B and C == A :
        return a + b + 2

def main():
    print(solve())

if __name__ == '__main__':
    main()