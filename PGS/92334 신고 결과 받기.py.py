def solution(id_list, report, k):
    id_dic = {}
    block = []  
    for id in id_list:
        id_dic[id] = [0,[]]    #[신고 당한 횟수,[key를 신고한 유저목록]
    for re in report:
        user1, user2 = re.split()
        if user2 not in id_dic[user1][1]:
            id_dic[user1][1].append(user2)  #[user2가 신고한 유저, user1이 신고 당한 유저]
            id_dic[user2][0] += 1  
            if id_dic[user2][0] == k:       #2번 이상 신고당하면 정지라서 2일때만 정지리스트에 모으기
                block.append(user2)
    # print(id_dic)
    # print(block)
    answer = [0] *(len(id_list))
    for id2 in range(len(id_list)):          #유저 수만큼 돌리기
        for id3 in id_dic[id_list[id2]][1]:  #내가 신고했던 유저 목록 보면서
            if id3 in block:                 #정지당했다면 메일받기 (answer += 1)
                answer[id2] += 1
    return answer

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))