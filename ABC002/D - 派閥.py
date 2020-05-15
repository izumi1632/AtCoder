import itertools

N , M = map(int, input().split())
relations = set()

for i in [list(map(int, input().split())) for i in range(M)]:
  relations.add((i[0], i[1]))

m = 0
for i in range(2**N):
  #人間関係を無視した全パターン列挙
  people = []
  for j in range(N):
    if (i >> j) & 1:
      people.append(j + 1)

  if set(itertools.combinations(people, 2)) <= relations:
    m = max(m, len(people))

print(m)