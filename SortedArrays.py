N = int(input())
A = list(map(int, input().split()))

count = 1
first = True
isIncrease = False
for i in range(1, len(A)):
    if first == True:
        if A[i] > A[i - 1] :
            isIncrease = True
            first = False
        elif A[i] < A[i - 1] : 
            isIncrease = False
            first = False
    else:
        if isIncrease == True and A[i] < A[i - 1]:
            isIncrease = False
            count += 1
            first = True
        elif isIncrease == False and A[i] > A[i - 1]:
            isIncrease = True
            count += 1
            first = True
            
print(count)