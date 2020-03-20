N = int(input())
list = sorted(list(map(int, input().split())),reverse=True)
print(sum(list[::2])- sum(list[1::2]))






