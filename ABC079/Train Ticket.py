A,B,C,D = input('')
for i in range(2**3):
  op = [0] * 3
  for j in range(3):
    if (i >> j) & 1:
      op[j]='+'
    else:
      op[j]='-'
  if eval(A+op[0]+B+op[1]+C+op[2]+D)==7:
    print(A+op[0]+B+op[1]+C+op[2]+D+'=7')
    exit()
    