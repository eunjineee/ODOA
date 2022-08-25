N = input()
note1 = set(map(int, input().split()))
M = input()
note2 = list(map(int, input().split()))

for i in note2:
    if i in note1:
        print(1)
    else:
        print(0)