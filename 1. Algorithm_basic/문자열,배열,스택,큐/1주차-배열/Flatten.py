
def maxmax(data):
    max_value = 0
    max_idx = -1
    for i in range(len(data)):
        if data[i] > max_value:
            max_value = data[i]
            max_idx = i
    return max_idx

def maxmax():
    max_value = 0
    max_idx = 0
    for i in range(len(data)):
        if data[i] > max_value:
            max_value = data[i]
            max_idx = i
    return max_idx

def minmin():
    min_value = 123456
    min_idx = 0
    for k in range(len(data)):
        if data[k] < min_value:
            min_value = data[k]
            min_idx = k
    return min_idx

for j in range(1, 11):
    N = int(input())
    data = list(map(int, input().split()))

    for h in range(N):
        data[maxmax()] -= 1
        data[minmin()] += 1

    print('#{} {}'.format(j, data[maxmax()] - data[minmin()]))
#  --------------------------------------------

for i in range(1, 11):
    N = int(input())
    TC = list(map(int, input().split()))
    ans = 0
    for h in range(N):
        for k in range(len(TC), 0, -1):
            for j in range(k):
                if TC[j] > TC[j+1]:
                    TC[j], TC[j+1] = TC[j+1], TC[j]

        TC[-1] -= 1
        TC[0] += 1

        ans = TC[-1] - TC[0]

    print('#{} {}'.format(i, ans))

# ---------------------------------

def bubble(yo):
    for i in range(len(yo)-1, 0, -1):
        for k in range(i):
            if yo[k] > yo[k+1]:
                yo[k], yo[k+1] = yo[k+1], yo[k]
    return yo

for i in range(1, 11):
    N = int(input())
    data = list(map(int, input().split()))
    ans = 0

    for k in range(N):
        bubble(data)
        data[-1] -= 1
        data[0] += 1

    bubble(data)
    ans = data[-1] - data[0]
    print('#{} {}'.format(i, ans))





