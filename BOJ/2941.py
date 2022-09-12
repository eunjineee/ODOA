cr = ['c=','c-','dz=','d-','lj','nj','s=','z=']

n = input()
cnt = 0

while len(n) != 0:
    if n[0:2] in cr:
        cnt += 1
        n = n[2:]
    elif n[:3] in cr:
        cnt += 1
        n = n[3:]
    else:
        cnt += 1
        n = n[1:]

print(cnt)