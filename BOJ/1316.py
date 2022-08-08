a = int(input())
total = 0
for i in range(a):
    b = list(input())      
    if len(b) > 2:
        for j in range(1,len(b)):
            if b[j] != b[j-1]:
                if b[j-1] in b[j::]:
                    break
            if len(b)-1 == j :
                total += 1
    else:
        total +=1
print(total)