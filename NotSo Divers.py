from collections import Counter
N,K = map(int,input().split())
A = sorted(Counter(map(int, input().split())).items(), key=lambda x:x[1], reverse=False)
s = len(A) - K
c = 0
if s > 0:
    for i in range(s):
        c += A[i][1]
print(c)
