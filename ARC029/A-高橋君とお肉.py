N = int(input())
t = list([int(input()) for i in range(N)])
minTime = 50*4
# ビットの位置でどちらの肉や機器を使用するか判断
for i in range(2**N):
  time = [0 for i in range(2)]
  for j in range(N):
    if (i >> j) & 1:
      time[0] += t[j]
    else:
      time[1] += t[j]
  minTime = min (minTime, max(time[0],time[1
  ]))
print(minTime)