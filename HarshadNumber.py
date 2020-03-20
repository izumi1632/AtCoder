def getSum(N):
    s = 0
    while N > 0:
        s += N % 10
        N = int(N / 10)
    return s
def main():
    N = int(input())
    if N % getSum(N) == 0:
        print('Yes')
    else:
        print('No')

main()

