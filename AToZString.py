s , e = -1 , 0
c =  0
for i in input():
    if i == 'A':
        if s == -1:
            s = c
        
    if i == 'Z':
        e = c

    c += 1

print(e-s+1)