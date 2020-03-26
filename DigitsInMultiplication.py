N = int(input())
n = round(N ** 0.5)
m = 12
for i in range(1, n + 1):
    if N % i == 0:
        j = N // i
        #print('{0} , {1}'.format(i,j))
        m = min(max(len(str(i)),len(str(j))),m)
print(m)