



def calc(v):
    if len(tree[v]) == 2:
        return tree[v][1]
    else:
        L = calc(tree[v][2])
        R = calc(tree[v][3])

        if tree[v][1] == '+': return L+R
        elif tree[v][1] == '-': return L-R
        elif tree[v][1] == '*': return L*R
        elif tree[v][1] == '/': return L/R


for tc in range(1, 11):
    n = int(input())  #정점의 개수
    tree = [0] * (n+1)

    for i in range(n):
        tmp = input().split()
        tree[int(tmp[0])] = tmp

        # 두 가지 갈림길
         # 1. 먼저 처리를 하고 가자
        ## tmp 길이가 4일 때, 0번 인덱스: 정점번호, 1번: 연산자, 2번:왼, 3번: 오른
        if len(tmp) == 4:
            tree[int(tmp[0])][2] = int(tree[int(tmp[0])][2])
            tree[int(tmp[0])][3] = int(tree[int(tmp[0])][3])
        else:
            tree[int(tmp[0])][1] = int(tree[int(tmp[0])][1])
    print(tree)
    print('#{} {}'.format(tc, int(calc(1))))


######################################


def calc(v):
    if len(tree[v]) == 2:
        return int(tree[v][1])
    else:
        L = calc(int(tree[v][2]))
        R = calc(int(tree[v][3]))

        if tree[v][1] == '+': return L+R
        elif tree[v][1] == '-': return L-R
        elif tree[v][1] == '*': return L*R
        elif tree[v][1] == '/': return L/R


for tc in range(1, 11):
    n = int(input())  #정점의 개수
    tree = [0] * (n+1)

    for i in range(n):
        tmp = input().split()
        tree[int(tmp[0])] = tmp


    print('#{} {}'.format(tc, int(calc(1))))