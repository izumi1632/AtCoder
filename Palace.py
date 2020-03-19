N = input()
TA = input().split()
T = int(TA[0])
A = int(TA[1])

first = True
place = 0
minTmep = 0

H = list(map(int, input().split()))
for i in range(0,len(H)):
    compare = abs(A * 1000 - (T * 1000 - H[i] * 0.006 * 1000))
    if first == True:
        place = i
        minTmep = compare
        first = False
    
    if minTmep > compare:
        place = i
        minTmep = compare

print(place + 1)