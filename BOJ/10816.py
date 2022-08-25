N = int(input())
note1 = list(map(int,input().split()))
M = int(input())
note2 = list(map(int, input().split()))
new_dict = {}

for num in note1:
    if num in new_dict:
        new_dict[num] += 1
    else:
        new_dict[num] = 1

for i in note2:
    if i in new_dict:
        print(new_dict[i],end=' ')
    else:
        print(0,end=' ')