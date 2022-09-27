for i in range(101):
    for j in range(i, 0, -1):
        if sum(list(map(int,list(str(i))))) + j == i:
            break
    else:
        print(i)
