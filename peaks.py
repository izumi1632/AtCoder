N,M = map(int,input().split())

H = list(map(int,input().split()))

a = [True for i in range(N)]

for i in range(M):
  A,B = map(int, input().split())
  if H[A-1] < H[B-1]:
    a[A-1] = False
  elif H[A-1] > H[B-1]:
    a[B-1] = False
  elif H[A-1]== H[B-1]:
    a[A-1] = False
    a[B-1] = False

print(len([0 for i in a if i == True]))