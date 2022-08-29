from sys import stdin

#입력
T = int(stdin.readline())
#중첩 리스트 두 개 - 각 케이스의 나라&비행기수, 비행기목록
course = []
airplane = []
for i in range(T) : 
    course.append(list(map(int, stdin.readline().split())))
    t = []
    for j in range(course[i][1]) :
        t.append(list(map(int, stdin.readline().split())))
    airplane.append(t)
# print(course)
# print(airplane)

#연결리스트임 - 모든 비행기가 연결되어있으므로 그냥 방문해야 하는 나라 - 1 하면 됨
for i in range(T) :
    print(course[i][0]-1)