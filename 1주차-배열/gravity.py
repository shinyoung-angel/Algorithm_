for i in range(1, int(input())+1):
    #박스 갯수
    N = int(input())
    box = list(map(int, input().split()))  # 입력 받음

    ans = 0

    # 전체 모든 박스 비교
    for i in range(N):
        cnt = 0

        # 작은 값을 찾아 카운트
        for j in range(i+1, N):
            if box[i] > box[j]:
                cnt += 1

        if ans < cnt:
            ans = cnt


    print(f'#{i} {ans}')


