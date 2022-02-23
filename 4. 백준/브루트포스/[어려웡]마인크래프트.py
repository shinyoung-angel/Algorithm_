import sys
input = sys.stdin.readline

#### 최대 높이가 256이라 완전탐색은 생각도 못했다,,!
#### 고러나 500*500*256 은 완탐으로 가능했다,,!
#### 하지만 python말고 pypy3로 가능하다는 거,,

n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]
min_time = 10000000000000000000000000000000000000000000
min_num = min(map(min, ground))
max_num = max(map(max, ground))
min_num = min_num if min_num >= 0 else 0
max_num = max_num if max_num <= 256 else 256

for value in range(min_num, max_num+1):
    inventory_add = 0
    gonna_use = 0
    for j in range(n):
        for k in range(m):
            tmp = ground[j][k]
            if tmp > value:
                inventory_add += tmp - value
            else:
                gonna_use += value - tmp
    inventory = b + inventory_add
    if inventory < gonna_use:
        continue
    time = inventory_add * 2 + gonna_use
    if time <= min_time:
        min_time = time
        height = value

print(min_time, height)







# 틀렸습니다!ㅠㅠㅠㅠㅠㅠㅠㅠㅠ
#### 시도 1:
#### 분기를 한다
#### 땅의 높이를 최저에 맞출지, 최고에 맞출지
#### 그리고 필요한 땅의 크기를 각각 비교하고 최소값을 찾음
#### 이후 필요에 따라 또다시 분기

n, m, b = map(int, input().split())
ground = []
max_num = 0
min_num = 256
max_need = 0
min_need = 0

def check ():
    global max_num

    flag = 0
    extract = 0
    add = 0

    while flag == 0:

        max_num -= 1
        for i in range(n):
            for j in range(m):
                tmp = ground[i][j]
                if tmp > max_num:
                    extract += tmp - max_num
                    tmp -= (tmp-max_num)
                else:
                    add += max_num - tmp
                    tmp += (max_num-tmp)
        if extract+b >= add:
            flag = 1
            second = extract * 2 + add
            tall = max_num

    return [second, tall]



# for _ in range(n):
#     tmp = list(map(int, input().split()))
#     max_num = max(max_num, max(tmp))
#     min_num = min(min_num, min(tmp))
#     ground.append(tmp)
#
# max_num = max_num if max_num <= 256 else 256
# min_num = min_num if min_num >= 0 else 0
#
# ### 최대 높이에 맞추기
# for i in range(n):
#     for j in range(m):
#         tmp = ground[i][j]
#         max_need += max_num - tmp
#         min_need += tmp - min_num
#
# need = min(max_need, min_need)
#
# time = 1
# if need == min_need:
#     time = min_need * 2
#     height = min_num
#     print(time, height)
# else:
#     height = max_num
#     if need <= b:
#         print(need, height)
#     else:
#         print(*check())

