import sys
input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]

################# 정렬을 두 번 해줘야 함~~~~~~~~~~~~~~~~~~~~~
######## 끝나는 시간 기준으로만 정렬했다면 오답!
## 11 11
## 9 11
## 위와 같은 시간이 있을 경우를 고려해야 함!
## 1. 시작 시간을 기준으로 오름차순
## 2. 끝나는 시간을 기준으로 오름차순
time.sort()
time.sort(key= lambda x: x[1])


now = time[0][1]
ans = 1
for i in range(1, n):
    tmp = time[i][0]

    if tmp >= now:
        now = time[i][1]
        ans += 1


print(ans)



