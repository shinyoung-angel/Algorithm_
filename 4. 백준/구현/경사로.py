import sys
input = sys.stdin.readline

def check(line):
    visited = [0] * n

    for i in range(n-1):
        extract = line[i] - line[i+1]   ## 앞뒤의 차이

        if abs(extract) >= 2: return 0 ## 2이상은 ㄴㄴ
        elif extract == 0: continue    ## 같다면 통과~
        elif extract == 1:             ## 다음 칸이 descend
            temp = line[i+1]           ## 바로 다음 칸부터 다음칸+l칸 까지 평평해야 함 == 층이 같아야 함
            for j in range(i+1, i+1+l):
                if 0 <= j < n:         ## 범위 안에 있을 때
                    if line[j] != temp: return 0    ## 평평하지 않다면 ㄴㄴ
                    if visited[j] == 1: return 0    ## 이미 경사로가 있다면 ㄴㄴ
                else:
                    return 0           ## 범위를 벗어났다면 ㄴㄴ
                visited[j] = 1         # 해당 없다면 경사로 방문 췤


        elif extract == -1:             ## 다음 칸이 ascend
            temp = line[i]              ## 해당칸부터 해당칸 - l 칸까지 평평해야 함
            for j in range(i, i-l, -1):
                if 0 <= j < n:
                    if line[j] != temp: return 0
                    if visited[j] == 1: return 0
                else:
                    return 0
                visited[j] = 1

    return 1


n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0


## 가로 검사
for k in arr:
    cnt += check(k)

## 세로 검사
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(arr[j][i])
    cnt += check(tmp)

print(cnt)



