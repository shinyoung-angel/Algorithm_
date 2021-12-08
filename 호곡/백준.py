#
# def move():
#     check = {}
#     dirs = [0, (-1 ,0), (1 ,0), (0 ,-1), (0 ,1)]
#     rdirs = [0, 2, 1, 4, 3]
#     for th in range(K):
#         microbe = microbes[th]
#         y, x, num, loc = microbe
#         if num == 0:
#             continue
#         # 이동
#         ny, nx = y+ dirs[loc][0], x + dirs[loc][1]
#         microbe[0], microbe[1] = ny, nx  # 새 위치 할당
#         # 약품확인
#         if ny == 0 or nx == 0 or ny == (N - 1) or nx == (N - 1):
#             microbe[2] = microbe[2] // 2  # 생물 수 1/2
#             microbe[3] = rdirs[microbe[3]]  # 방향 반대로
#         # 겹치는지 확인
#         if (ny, nx) not in check:
#             check[(ny, nx)] = (th, num)
#             continue
#         # 겹치면
#         bth, bnum = check[(ny, nx)]
#         if bnum < num:  # 클 때
#             check[(ny, nx)] = (th, num)  # 일단 리스트에 등록
#             microbe[2] += microbes[bth][2]  # 흡수
#             microbes[bth][2] = 0
#         else:  # 작을 때
#             microbes[bth][2] += microbe[2]  # 흡수당함
#             microbe[2] = 0
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M, K = map(int, input().split())
#     microbes = [list(map(int, input().split())) for _ in range(K)]
#     res = 0
#     for _ in range(M):  # 초마다 위치 갱신
#         move()
#     for f in range(K):
#         res += microbes[f][2]
#     print('#{} {}'.format(tc, res))


import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if i in n_list:
        print(1)
    else:
        print(0)


