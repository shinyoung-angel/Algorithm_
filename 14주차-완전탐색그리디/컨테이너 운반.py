

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    ## 내림차순으로 무게와 적재용량을 정렬
    weight = sorted(list(map(int, input().split())), reverse=True)
    truck_capacity = sorted(list(map(int, input().split())), reverse=True)

    # 가능한 컨테이너 무게의 합
    total_weight = 0

    # 트럭의 갯수만큼 반복함
    for i in range(m):
        truck = truck_capacity[i]

        ## 트럭의 적재용량이 컨테이너 무게보다 크거나 같다면 total_weight에다가 추가해줌.
        ## 그리고 다음 계산을 위해 해당 컨테이너 무게를 pop해줌.
        for j in range(len(weight)):
            if truck >= weight[j]:
                total_weight += weight[j]
                weight.pop(j)
                break
        ## 예외처리
        else:
            continue

    print('#{} {}'.format(tc, total_weight))

