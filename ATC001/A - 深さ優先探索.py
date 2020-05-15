import sys
import itertools
# sys.setrecursionlimit(1000000000)

H, W = map(int, input().split())
cw = list([list(' '.join(input()).split()) for i in range(H)])
mapCW = list([[False for j in range(W)] for i in range(H)])
flg = False


def solve():
  #スタート地点
  start = set()
  for i in range(H):
    for j in range(W):
      if cw[i][j] == 's':
        startX = i
        startY = j
  return ss(startX, startY)

def ss(i, j):

  if cw[i][j] == 'g':
    global flg
    flg = True
    # print('Yes')
    # exit()
    # return True
  if cw[i][j] == '#':
    return
    # return False

  cw[i][j] = '#'
  for c in range(-1, 2):
    for w in range(-1, 2):
      if canMove(c+i, w+j) and (c == 0 or w == 0) and (c == 1 or c== -1 or w == 1 or w == -1):
        mapCW[c+i][w+j] = ss(c+i, w+j)
  return

def canMove(i, j):
  return (0 <= i < H) and (0 <= j < W) and (cw[i][j] != '#')

solve()
print('Yes' if flg else 'No')