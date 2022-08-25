N = int(input())
note1 = list(map(int,input().split()))
M = int(input())
note2 = list(map(int, input().split()))
new_dict = {}

for num in note2:
    if num in new_dict:
        new_dict[num] += 1
    else:
        new_dict[num] = 1

print(new_dict.values())