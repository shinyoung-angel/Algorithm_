
# 가위 1, 바위 2, 보3

def win(num_a, rcp_a, num_b, rcp_b):
    # 가위바위보가 위의 숫자처럼 정해여 있으니 활용 가능
    if rcp_b - rcp_a == 1 or rcp_b - rcp_a == -2:  # b가 이겼을 경우
        return num_b, rcp_b
    else: # b가 비기거나 진 경우
        return num_a, rcp_a

def divided(st, ed):
    # 한 사람만 남았을 때
    if st == ed:
        return st, people[st]
    mid = (st +ed) // 2

    return win(*divided(st, mid), *divided(mid +1, ed))

T = int(input())

for tc in range(1, T+ 1):
    N = int(input())
    people = list(map(int, input().split()))

    ans = divided(0, N - 1)

    print('#{} {}'.format(tc, ans[0] + 1))


# -----------

def RPS(lst):
    if len(lst) == 1:
        return lst[0][0], lst[0][1]
    else:
        student1, rpc1 = RPS(lst[:(len(lst) - 1) // 2 + 1])
        student2, rpc2 = RPS(lst[(len(lst) - 1) // 2 + 1:])

        if rpc2 - rpc1 == 1 or rpc2 - rpc1 == -2:
            return student2, rpc2
        else:
            return student1, rpc1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    card = list(enumerate(map(int, input().split())))  # 1: 가위, 2: 바위, 3: 보

    print('#{} {}'.format(tc, RPS(card)[0] + 1))