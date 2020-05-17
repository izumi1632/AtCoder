N,M = map(int,input().split())
uv = list([set(list(map(int, input().split()))) for i in range(M)])
# print(uv)

# 到達履歴
mapUV = [i for i in range(1, M + 1)]
count = 0
def solve():
  #とりあえず１からスタート
  global mapUV
  mapUV.remove(1)
  dfs(1)

def dfs(i):
  # 移動可能な箇所を探す
  global uv
  for t in uv:
    if i in t:
      next = [j for j in t if i != j][0]
      if next not in mapUV:
        global count
        count += 1
        return False
      uv.remove(([m for m in uv if i in m and next in m])[0])
      dfs(next)
  return True

solve()
print(count)


