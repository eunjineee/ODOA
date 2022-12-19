import sys
input = sys.stdin.readline
n = int(input())
dict = {}
ans = []
ans_people = 0
ans_people_not = 0
for _ in range(n):
    num, user_id, answer, memory, time, lan, length = input().split()
    if user_id == 'megalusion':
        continue
    if user_id in dict:
        if dict[user_id][0] == True:
            continue
        else:
            if answer != '4':
                dict[user_id][1] += 1          
            else:
                dict[user_id][0] = True
                ans.append(user_id)
                ans_people_not += dict[user_id][1]
                ans_people += 1
    else:
        if answer != '4':
            dict[user_id] = [False, 1]
        else:
            dict[user_id] = [True, 1]
            ans.append(user_id)
            ans_people += 1
if ans_people == 0:
    print(0)
else:
    ans_ratio = ans_people / (ans_people + ans_people_not) *100
    print(ans_ratio)
