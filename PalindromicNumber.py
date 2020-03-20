A, B = map(int, input().split())
c = 0
for i in range(A, B + 1):
    if str(i) == str(i)[::-1]:
        c += 1
print(c)