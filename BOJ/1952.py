T = int(input())
for t in range(T):
    price = list(map(int, input().split()))
    day = list(map(int, input().split()))
    total = [0]*12
    
    for d in range(12):
        if price[0] * day[d] >= price[1]:
            total[d] = price[1]
        else:
            total[d] = day[d]*price[0]
    
    testcase = []
    for d in range(12):
        test = total[:]
        while d <= 12:
            if sum(test[d-2:d+1]) > price[2]:
                try:
                    test [d-2] = price[2]
                    test [d-1] = 0
                    test [d] = 0
                except IndexError:
                    continue
            d += 3
        testcase.append(sum(test))
    for d in range(12):
        test = total[:]
        while d <= 12:
            if sum(test[d-2:d+1]) > price[2]:
                try:
                    test [d-2] = price[2]
                    test [d-1] = 0
                    test [d] = 0
                except IndexError:
                    continue
            d += 4
        testcase.append(sum(test))
    for d in range(12):
        test = total[:]
        while d <= 12:
            if sum(test[d-2:d+1]) > price[2]:
                try:
                    test [d-2] = price[2]
                    test [d-1] = 0
                    test [d] = 0
                except IndexError:
                    continue
            d += 5
        testcase.append(sum(test))
        
    to = min(testcase)
    if to > price[3]:
        to = price[3]
    print(f'#{t+1} {to}')