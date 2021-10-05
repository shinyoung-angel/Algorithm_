

### 회의실 문제 생각하다가 변수를 회의실 문제로 설정해버림.

for tc in range(1, int(input())+1):
    n = int(input())
    time = [list(map(int, input().split())) for _ in range(n)]
    ## 종료 시간을 기준으로 정렬해줌
    time.sort(key=lambda x:x[1])

    # 이미 정렬이 되어있는 상태이기 때문에 가장 첫 번째 회의가 가장 빨리 끝남. 그래서 meeting이라는 변수에 담아둠.
    meeting = time[0]
    # meeting에 하나가 담겨있으니 회의 1개를 카운트
    cnt = 1
    ## 전체 회의 수만큼 반복할 것임
    ### 다음 회의 시작 시간이 이전 회의 끝나는 시간보다 크거나 같으면 카운트하고 meeting을 갱신
    for i in range(1, n):
        if time[i][0] >= meeting[1]:
            cnt += 1
            meeting = time[i]


    print('#{} {}'.format(tc, cnt))






