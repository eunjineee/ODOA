T = int(input())

for test_case in range(1, T+1):
    N =int(input())
    arr = list(map(int, input()))
    for i in range(1, N):
         arr[i] = arr[i-1] * arr [i] + arr[i]
    print(f'#{test_case} {max(arr)}')