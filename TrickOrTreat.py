N,K = map(int,input().split())

s = set()

#K種類ループ
for i in range(K):
  d = int(input())
  ad = list(map(int,input().split()))
  for a in range(d):
    s.add(ad[a])

print(N - len(s))