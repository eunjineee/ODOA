import sys
N = int(sys.stdin.readline().rstrip())

num = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]
    l,m,e = [], [], []
    for each in nums:
        if each < pivot:
            l.append(each)
        elif each > pivot:
            m.append(each)
        else:
            e.append(each)
    return quick_sort(l) + e + quick_sort(m)
num = quick_sort(num)

for i in num:
    print(i)
