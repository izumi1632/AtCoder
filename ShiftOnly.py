N = int(input())
list = list(map(int, input().split()))
c = 0
b = True

while b == True:
    for i in range(0,len(list)):
        if list[i] % 2 != 0:
            b = False
        else:
            list[i] = list[i] / 2
    if b == False:
        break
    c += 1

print(c)