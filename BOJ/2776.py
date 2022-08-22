def ejin(arr, target):
        f, l = 0, len(note1)-1
        while f <= l:
            m = (f+l) // 2
            if note1[m] > target:
                l = m -1
            if note1[m] == target:
                return 1
            if note1[m] < target:
                f = m + 1
        return 0

T = int(input())
for t in range(T):
    N = int(input())
    note1 = list(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))
    note1.sort()
    for i in note2:
        print(ejin(note1,i))
        

    