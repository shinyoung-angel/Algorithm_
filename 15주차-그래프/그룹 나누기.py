
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


