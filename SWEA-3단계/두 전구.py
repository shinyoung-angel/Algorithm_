
T = int(input())
ans = []
for tc in range(1, T+1):
    a, b, c, d = map(int, input().split())
    result = 0
    maxi = max(a,c)
    mini = min(b,d)
    if maxi < mini:
        result = len(range(maxi, mini))
    ans.append(result)

for i in range(T):
    print('#{} {}'.format(i+1, ans[i]))

