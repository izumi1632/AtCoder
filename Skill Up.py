N, M, X = map(int,input().split())

CAM = list([list(map(int,input().split())) for i in range(N)])
# print(CAM)
minn = 10**18
b = False

for i in range(2 ** N):
  s = 0
  am = []

  for j in range(N):  # このループが一番のポイント
      if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
        am.append(CAM[j])

  j = False
  sss = [0] * (M+1)
  for kk in range(len(am)):
    s += am[kk][0]
    for m in range(0, M):
      sss[m+1] += am[kk][m+1]
  
  if len([i for i in sss[1:] if i >= X] ) == len(sss[1:]):
    b = True
    minn = min(s,minn)
  
  # print(sss)
  # if x >= X and y >= X and z >= X:
  #   minn = min(s,minn)
  #   b = True

print(minn if b == True else -1)