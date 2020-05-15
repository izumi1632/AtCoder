N,K = map(int, input().split())
A = list(map(int, input().split()))

c = 1
city = 1
s = set()
s.add(city)

while True:

  city = A[city - 1]
  if city in s:
    print(A[(K%len(s))])

    exit()

  s.add(city)
  if c == K:
    print(city)
    exit()

  c += 1


