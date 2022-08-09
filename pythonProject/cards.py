import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1,T+1):
    N = int(input())
    Nli = input()
    card_list = [0] * 10
    num = top = 0
    for n in Nli:
        card_list[int(n)] += 1
    for x in range(9,0,-1 ):
        if top < card_list[x]:
            top = card_list[x]
            num = x
    print(f'#{t} {num} {top}')