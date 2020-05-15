import itertools
N,M,Q = map(int, input().split())
a = itertools.combinations_with_replacement(([i for i in range(1,M+1)]), N)
abcdQ = [list(map(int, input().split())) for i in range(Q)]
maxSumD = 0
for A in a:
  sumD = 0
  for abcd in abcdQ:
    if A[abcd[1]-1]-A[abcd[0]-1] == abcd[2]:
      sumD += abcd[3]
  maxSumD = max(maxSumD, sumD)
  
print(maxSumD)