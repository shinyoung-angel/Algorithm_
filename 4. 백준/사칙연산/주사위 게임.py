import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int ,input().split())) for _ in range(n)]
result = []
for i in range(n):
    tmp = arr[i]
    num_dic = {i:0 for i in tmp}

    for j in tmp:
        num_dic[j] += 1


    max_num = 0
    max_cnt = 1
    for key, value in num_dic.items():
        if value > max_cnt:
            max_cnt = value
            max_num = key

    ans = max(tmp) * 100
    if max_cnt == 3:
        ans = 10000 + (max_num*1000)
    elif max_cnt == 2:
        ans = 1000 + (max_num*100)
    result.append(ans)

print(max(result))
