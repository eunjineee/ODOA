def solution(string):
    answer = []
    ans_dict = {}
    num = 0
    while len(string) > 0:
        if num >= len(string)-1:
            if string[num] in ans_dict and string[0] not in answer:
                answer.append(string[num])
            break
        
        if string[num+1] != string[num]:
            if string[num] in ans_dict:
                answer.append(string[num])
            else:
                ans_dict[string[num]] = 1
            string = string[num+1:]
            num = 0
        else:
            num += 1
    if len(answer) == 0:
        return 'N'
    else:
        return ''.join(sorted(list(set(answer))))

print(solution('edeaaabbccd'))
print(solution('eeddee'))
print(solution('string'))
print(solution('zbzbz'))