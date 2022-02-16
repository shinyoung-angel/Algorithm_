import sys
input = sys.stdin.readline

## 처음 문제를 읽고 바로 dp네~ 하고 홀라당 풀었다가
## 홀라당 풀 문제가 아님을 자각했다

## tc가 무려 100,000개 이기 때문에
## 기존의 dp처럼 모든 배열을 들고다닐 수 x
## 따라서 필요한 정보인 배열 4개만 값을 계속 갱신해야 함

n = int(input())

## 현재 dp로 계산할 행의 바로 위의 행 정보
max_tmp = [0] * 3
min_tmp = [0] * 3

for i in range(n):
    a, b, c = map(int, input().split())
    ## 현재 값을 바꿔줘야하는 정보
    maxi = [0] * 3
    mini = [0] * 3

    for j in range(3):

        if j == 0:
            maxi[0] = a + max(max_tmp[0], max_tmp[1])
            mini[0] = a + min(min_tmp[0], min_tmp[1])
        elif j == 1:
            maxi[1] = b + max(max_tmp)
            mini[1] = b + min(min_tmp)
        elif j == 2:
            maxi[2] = c + max(max_tmp[1], max_tmp[2])
            mini[2] = c + min(min_tmp[1], min_tmp[2])

    ## 값의 갱신이 필요!!!
    max_tmp = maxi
    min_tmp = mini


print(max(maxi), end=' ')
print(min(mini))





##### 이렇게 풀면 메모리 초과임니다~~~~~~~~
##### 모든 배열을 들고다니면 앙대오~~~~~~~

import copy
import sys
input = sys.stdin.readline

n = int(input())

max_dp = [list(map(int, input().split())) for _ in range(n)]
min_dp = copy.deepcopy(max_dp)

for i in range(1, n):
    for j in range(3):
        now_max = max_dp[i][j]
        now_min = min_dp[i][j]
        if j == 0:
            max_dp[i][j] = now_max + max(max_dp[i-1][j], max_dp[i-1][j+1])
            min_dp[i][j] = now_min + min(min_dp[i - 1][j], min_dp[i - 1][j + 1])
        elif j == 1:
            max_dp[i][j] = now_max + max(max_dp[i-1])
            min_dp[i][j] = now_min + min(min_dp[i-1])
        elif j == 2:
            max_dp[i][j] = now_max + max(max_dp[i-1][j-1], max_dp[i-1][j])
            min_dp[i][j] = now_min + min(min_dp[i - 1][j-1], min_dp[i - 1][j])

print(max(max_dp[n-1]), end=' ')
print(min(min_dp[n-1]))