
def binary_search(num):

    st = 0
    ed = n-1
    flag = 0                    # 한 방향으로만 가는지 췤

    while st <= ed:

        mid = (st+ed) // 2

        if a[mid] == num:
            return 1

        elif a[mid] > num:
            ed = mid -1
            if flag == 1:       # 찾아야하는 값이 중간값보다 작다면
                break           # flag에다가 1을 줄 것인데
            flag = 1            # 이전에도 flag가 1이라는 것은 같은 방향이란는 말이니 break

        else:
            st = mid+1
            if flag == 2:
                break
            flag = 2

    return 0



for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    cnt = 0

    for i in b:
        if binary_search(i):                # 값을 찾았다면 카운트
            cnt += 1


    print('#{} {}'.format(tc, cnt))

# ------------------------------

#재귀

def binary_search_recurrsion(l,r, d, key):

    if l >r: return 0               # 교차하면 땡땡
    else:

        mid = (l+r)//2

        if key==a[mid]: return 1

        elif key < a[mid]:
            if d != 0:
                return binary_search_recurrsion(l, mid-1, 0, key)

        else:
            if d != 1:
                return binary_search_recurrsion(mid+1, r, 1, key)

    return 0


binary_search_recurrsion(0, n-1, -1, i )

