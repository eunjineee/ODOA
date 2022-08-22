def ejin(arr, target):
        f, l = 0, len(note1)-1
        while f <= l:
            m = (f+l) // 2
            if note1[m] > target:
                l = m -1
            if note1[m] == target:
                return 1
            if note1[m] < target:
                l = m + 1
        return 0

note1 = [1,2,3,4,5]
i=1

print(ejin(note1,i))