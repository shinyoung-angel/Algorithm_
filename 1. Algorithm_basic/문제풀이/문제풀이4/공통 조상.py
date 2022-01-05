

for tc in range(1, int(input())+1):
    v, e, a, b = map(int, input().split())
    arr = [[] for _ in range(v+1)]
    parent = [0] * (v+1)

    num = list(map(int, input().split()))
    for i in range(e):
        parent = num[2*i]
        child = num[2*i+1]
        arr[parent].append(child)
        arr[child].append(parent)

