A,B,C,X,Y = map(int, input().split())
m = max(A*X + B * Y,max(X,Y)* C)

# iはハーフの枚数０．５区切りでいらないので、２の倍数だけ買う
for i in range(0, max(X,Y) * 2 + 1, 2):
    
    # ハーフではなく、単品で必要な分
    a = max(0, X - i//2)
    b = max(0, Y - i//2)
    #print(i)
    m = min(m, a * A + b * B + i * C)

print(m)