def sumDigits(i):
    s = 0
    while i > 0:
        s += (i % 10)
        i = int(i / 10)
    return s
def main():
    N = int(input())
    m2 = 9 * 6
    for i in range(1, N + 1):
        k = N - i
        if k > 0:
            m2 = min(m2, sumDigits(i) + sumDigits(k))
    print(m2)

main()