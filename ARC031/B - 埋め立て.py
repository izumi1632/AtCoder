import copy
# 入力値
island = list([list(input()) for i in range(10)])
#丸の数を数えておく
num = sum([sum([1 for s in i if s =='o']) for i in island])
squareCount = 0
isAleady = [[False for i in range(10)] for j in range(10)]

def solve():
  # すべての×マスを◯に変える。すべてつながったかチェックする。
  # すべてのマスに対して試す。
  for i in range(10):
    for j in range(10):
      global island
      if island[i][j] == 'x':
        deepCopy = copy.deepcopy(island)
        island[i][j] = 'o'
        global squareCount
        squareCount = 0
        global isAleady
        isAleady = [[False for i in range(10)] for j in range(10)]
        dfs(i, j)
        # 元のマップにoを足しているため+１
        if squareCount == num + 1:
          return 'YES'
        island = deepCopy
  return 'NO'

def dfs(i, j):
  # 到達履歴
  isAleady[i][j] = True
  global squareCount
  squareCount += 1
  for n in range(-1, 2):
    for m in range(-1, 2):
      # 縦横のみ移動可能
      if ((n == 0 and m != 0) or (m == 0 and n != 0)):
        if canMove(i+n, j+m):
          dfs(i+n, j+m)

def canMove(i, j):
  global island
  return (0 <= i < 10 and 0 <= j < 10) and (isAleady[i][j] == False) and (island[i][j] == 'o')

print(solve())
