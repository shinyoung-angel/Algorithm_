import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]


ans = []
for i in range(n-8+1):                      ## 8*8 행렬만큼씩 필요함
    for j in range(m-8+1):
        start_B = 0
        start_W = 0

        for a in range(i, i+8):             ## 해당 행렬을 검사해줌
            for b in range(j, j+8):         ## 행,열 인덱스를 더했을 때 짝수일때/// 홀수일 때
                if (a+b) % 2 == 0:
                    if arr[a][b] != 'B': start_B += 1           ## 시작점이 블랙일 경우
                    if arr[a][b] != 'W': start_W += 1           ## 시작점이 화이트인 경우
                else:
                    if arr[a][b] != 'W': start_B += 1
                    if arr[a][b] != 'B': start_W += 1

        ans.append(start_B)
        ans.append(start_W)

print(min(ans))



