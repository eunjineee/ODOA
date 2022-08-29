nanjeong = []
for _ in range(9):
    nanjeong.append(int(input()))
total = sum(nanjeong)
nanjeong.sort()
for i in range(9):
    for j in range(i+1, 9):
        if total - nanjeong[i] - nanjeong[j] == 100:
            nanjeong.remove(nanjeong[i])
            nanjeong.remove(nanjeong[j-1])
            
            for m in nanjeong:
                print(m)
            exit()
        
