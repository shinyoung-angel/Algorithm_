#간단한 줄 알았더니 전혀 간단하지는 않았따,, ㅎ


N = int(input())
num = ['3', '6', '9']

for i in range(1, N+1):
    cnt = 0

    for j in str(i):
        if j in num:
            cnt += 1
    if cnt:
        i = '-' * cnt

    print(i, end=' ')
