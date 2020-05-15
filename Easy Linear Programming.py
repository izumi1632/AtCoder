A,B,C,K = map(int, input().split())

s = K - A
m = 0
if s >= 0:
  m += A
else:
  print(K)
  exit()
if s - B >= 0:
  s -= B
else:
  print(m)
  exit()
if s - C >= 0:
  print(m + (-C))
else:
  print(m - s)