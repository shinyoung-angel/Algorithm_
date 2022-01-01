
def make_set(x):
    p[x] = x

def find_set(x):

    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    p = [0] * (n+1)

    for i in range(1, n+1):
        make_set(i)

    partner = list(map(int, input().split()))

    for i in range(m):
        person1 = partner[i*2]
        person2 = partner[i*2+1]
        if person1 < person2:
            union(person1, person2)
        else:
            union(person2, person1)

    for i in range(1, n+1):
        find_set(i)

    ans = len(set(p)) - 1

    print('#{} {}'.format(tc, ans))



################


def dfs(x):

    visited[x] = 1

    for i in range(1, n+1):
        if arr[x][i] and not visited[i]:
            dfs(i)

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    partner = list(map(int, input().split()))
    arr = [[0]*(n+1) for _ in range(n+1)]
    visited = [0] * (n+1)

    for i in range(m):
        person1 = partner[i*2]
        person2 = partner[i*2+1]
        arr[person1][person2] = 1
        arr[person2][person1] = 1

    ans = 0
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            ans += 1

    print('#{} {}'.format(tc, ans))


#######################


def fine_set(x):
    while p[x] != x:
        x = p[x]
    return x

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    partner = list(map(int, input().split()))
    p = [i for i in range(n+1)]         # make_set 과정

    for i in range(m):
        a = partner[2*i]
        b = partner[2*i+1]

        p[fine_set(b)] = find_set(a)        ## union 함수없이 바로

    ans = 0

    for i in range(1, n+1):                 ## findset을 다시 해줄 필요 없이 p[x]와 x가 일치하는 갯수를 카운트
        if p[i] == i:
            ans += 1
    print('#{} {}'.format(tc, ans))