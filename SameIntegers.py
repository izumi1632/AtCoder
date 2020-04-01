ABC = list(sorted(map(int, input().split())))

# 最初にプラス1で近づける
A, B, C = ABC[0], ABC[1], ABC[2]
count = 0


a, amod = divmod((C-A),2)
b, bmod = divmod((C-B),2)

for i in range(C - B):
    A += 1
    B += 1
    count += 1



