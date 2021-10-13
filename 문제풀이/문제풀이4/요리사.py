


# for tc in range(1, int(input())+1):
#     n = int(input())
#     arr = [list(map(int, input().strip().split())) for _ in range(n)]
#     food_sum = set()
#
#     for i in range(n-1):
#         for j in range(i, n):
#             if i != j:
#                 food = arr[i][j] + arr[j][i]
#                 food_sum.add(food)
#
#     calculate = 0
#     synergy = 123456789
#     for i in range(len(food_sum)-1):
#         tmp = tuple(food_sum)[i]
#         for j in range(i+1, len(food_sum)):
#             calculate = abs(tmp - tuple(food_sum)[j])
#
#             if calculate < synergy:
#                 synergy = calculate
#
#     print(food_sum)
#     print('#{} {}'.format(tc, synergy))


# def comb(cnt, idx, start):  # 조합 찾기
#     # 현재 선택한 개수, p1의 값을 바꿔 줄 위치 값, 시작점
#
#     if cnt == find_num:  # 현재 선택한 개수가 찾으려는 숫자와 같은 경우
#         cal(0)
#         return
#
#     else:
#         for q in range(start, n):
#             p1[idx] = q
#             comb(cnt + 1, idx + 1, q + 1)  # 선택한 개수 + 1, 위치 + 1, 시작점은 현재 값 + 1
#     return
#
#
# def cal(p2_cnt):  # 계산
#     global min_res
#     customer1 = 0  # 고객 1의 합
#     customer2 = 0  # 고객 2의 합
#
#     for w in range(n):  # 고객 2의 재료 선택
#         if w not in p1:
#             p2[p2_cnt] = w
#             p2_cnt += 1
#
#     for i in range(n // 2):  # 계산하기, 홀수가 존재하기 때문에 하나씩 뽑아서 대조하면서 계산
#         # if n == 6이면 n//2 == 3이고, 두개씩 짝 지으면 한 개가 남아버림
#
#         for j in range(n // 2):
#             if i != j:  # 같은 값 제외 [1, 2]에서 1+1 같은 경우 배제하기 위함
#                 customer1 += foods[p1[i]][p1[j]]
#                 customer2 += foods[p2[i]][p2[j]]
#
#     if abs(customer1 - customer2) < min_res:  # min_res보다 작으면 값 바꾸기
#         min_res = abs(customer1 - customer2)
#
#     return
#
#
# T = int(input())
#
# for tc in range(1, 1 + T):
#     n = int(input())
#
#     foods = [list(map(int, input().split())) for _ in range(n)]  # 시너지 표
#
#     min_res = 20000 * n  # 최소 값, 시너지 최대 값 * n
#
#     p1 = [0] * (n // 2)  # 1번 고객의 재료를 저장하기 위함
#     p2 = [0] * (n // 2)  # 2번 고객의 재료를 저장하기 위함
#
#     find_num = n // 2  # 선택해야 할 개수
#
#     comb(0, 0, 0)  # 현재 선택한 개수, p1의 값을 바꿔 줄 위치 값, 시작점
#
#     print('#{} {}'.format(tc, min_res))


#########################################

def synergy():
    A_synergy = 0
    B_synergy = 0

    for t in range(N):
        for k in range(N):
            if chosen[t] and chosen[k]:
                A_synergy += test_case[t][k]
            elif not chosen[t] and not chosen[k]:
                B_synergy += test_case[t][k]

    return A_synergy, B_synergy


def choose_ingred(n=0, i=0):
    global ans

    if not ans:
        return

    if n == N // 2:
        s_A, s_B = synergy()
        if ans > abs(s_A-s_B):
            ans = abs(s_A-s_B)
        return

    for t in range(i, N):
        if ans and not chosen[t]:
            chosen[t] = 1
            choose_ingred(n+1, t)
            chosen[t] = 0


T = int(input().strip())

for tc in range(1, T+1):
    N = int(input().strip())
    test_case = [list(map(int, input().strip().split())) for _ in range(N)]
    chosen = [0] * N
    ans = 999999
    choose_ingred()

    print('#{} {}' .format(tc, ans))
