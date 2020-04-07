def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


A, B, C = map(int, input().split())
print('YES' if C % gcd(A, B) == 0 else 'NO')
