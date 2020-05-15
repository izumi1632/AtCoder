N = int(input())

A = [list(map(int,input().split())) for i in range(2)]

# 各マスの最大値を保持するマスを作成
Am = [[0 for j in range(N)] for i in range(2)]
# ループ内で処理するのめんどう
Am[0][0] = A[0][0]
Am[1][0] = A[0][0] + A[1][0]

# 1段目
for i in range(N):
  if i > 0:
    Am[0][i] = A[0][i] + Am[0][i-1]
# 2段目
for i in range(N):
  if i > 0:
    Am[1][i] = A[1][i] + max( Am[0][i] , Am[1][i - 1])


#print(Am)
print(Am[1][N-1])