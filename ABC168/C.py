import math

A,B,H,M = map(int,input().split())
rad = (H*30 + M * 0.5 )  - M * 6
a = A**2 + B**2 - (2 * A * B * math.cos(math.radians(rad)))
print(a**0.5)