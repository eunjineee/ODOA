import math

x,y,c = map(float, input().split())

start = 0
end = min(x,y)

while abs(start-end) > 1e-3:
    mid = (start + end) / 2
    h1 = math.sqrt(x**2 - mid**2)
    h2 = math.sqrt(y**2 - mid**2)
    h = (h1*h2)/(h1+h2)
    if c < h:
        start = mid
    else:
        end = mid

print(round(mid,3))