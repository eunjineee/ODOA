def solution(new_id):
    #1
    new_id = new_id.lower()
    new = ''
    #2
    for i in new_id:
        if i == '-' or i == '_' or i == '.':
            new += i
        elif i.isalpha() :
            new += i
        elif i.isdigit() :
            new += i
    new_id = new[0]
    #3
    for j in range(1,len(new)):
        if new[j-1] == '.' and new[j] =='.':
            pass
        else:
            new_id += new[j]
    #4
    if len(new_id) != 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if len(new_id) != 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    #5번
    if len(new_id) == 0:
        new_id = 'a'
    #6
    new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    #7
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]        
    answer = new_id
    return answer

# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
# print(solution("=.="))
# print(solution(	"123_.def"))
# print(solution("abcdefghijklmn.p"))
