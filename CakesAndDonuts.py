def main():
    N = int(input())

    for i in range(int(N / 4) + 1):
        for j in range(int(N / 7)+ 1):
            if i * 4 + j * 7 == N:
                print('Yes')
                return

    print('No')



main()