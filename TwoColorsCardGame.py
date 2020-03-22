from collections import Counter

N = Counter([input() for _ in range(int(input()))])
M = Counter([input() for _ in range(int(input()))])
print(max(0, max(N[key]-M[key] for key in N.keys())))
