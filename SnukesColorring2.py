W,H,N = map(int, input().split())
a = [0] * N
x = [0] * N
y = [0] * N

xl = 0
xr = W
yt = H
yb = 0

for i in range(N):
    x,y,a = map(int, input().split())
    if a == 1:
        xl = max(x,xl)

    elif a == 2:
        xr = min(x,xr)
    
    elif a == 3:
        yb = max(y,yb)    

    else :
        yt = min(y, yt)

# print(xr)
# print(xl)
# print(yt)
# print(yb)

ans = (xr - xl) * (yt - yb)
if ans <= 0 or ((xr - xl < 0 )or (yt - yb < 0)):
    ans = 0

print(ans)
        