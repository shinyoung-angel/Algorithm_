

for tc in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for i in range(n-3+1):
        new_list = arr[i:i+3]
        if new_list[1] != max(new_list) and new_list[1] != min(new_list):
            ans += 1

    print('#{} {}'.format(tc, ans))
