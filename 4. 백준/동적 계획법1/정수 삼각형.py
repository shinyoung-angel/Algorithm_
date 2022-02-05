import sys
input = sys.stdin.readline

n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

## 모든 요소에 최대값을 갱신해줘야 함
for i in range(1, n):   ##2번째 줄부터 끝까지
    for j in range(i+1): ##해당 리스트의 모든 요소들
        if j == 0:      ## 0번 인덱스는 전의 리스트의 0번 인덱스 + 본인의 값
            d[i][0] += d[i-1][0]
        elif j == i:
            d[i][j] += d[i-1][j-1]
        else:
            d[i][j] += max(d[i-1][j-1], d[i-1][j])

print(max(d[n-1]))