def solution(id_list, report, k):
    id_dic = {}
    block = []  
    for id in id_list:
        id_dic[id] = [0,[]]
    for re in report:
        user1, user2 = re.split()
        if user2 not in id_dic[user1][1]:
            id_dic[user1][1].append(user2)
            id_dic[user2][0] += 1  
            if id_dic[user2][0] == k:
                block.append(user2)
    # print(id_dic)
    # print(block)
    answer = [0] *(len(id_list))
    for id2 in range(len(id_list)):
        for id3 in id_dic[id_list[id2]][1]:
            if id3 in block:
                answer[id2] += 1
    return answer

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))