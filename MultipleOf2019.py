S = input()

s = []
c = 0
for i in range(0,len(S)):
  s.append(S[i])
  if int(("".join(s))) % 2019 == 0:
    c += 1
    s.clear()
    s.append(S[i])

print(c)