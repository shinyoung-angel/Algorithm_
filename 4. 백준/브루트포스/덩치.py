

## 나보다 큰 아이들을 count하는 문제다!!

n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]


for i in range(n):
    cnt = 1
    for j in range(n):
        ## 나보다 큰 아이들을 췤
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1

    print(cnt, end=' ')






