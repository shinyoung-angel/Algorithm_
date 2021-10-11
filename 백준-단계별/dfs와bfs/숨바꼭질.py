
# https://tooo1.tistory.com/111

def bfs():

    queue = [n]
    arr[n] = 1

    while queue:

        t = queue.pop(0)
        d = [-1, 1, t]

        if t == k:
            break

        for i in range(3):
            nt = t + d[i]

            if 0 <= nt < len(arr) and arr[nt] == 0:
                arr[nt] = arr[t] + 1
                queue.append(nt)


n, k = map(int, input().split())
arr = [0] * 100001
bfs()
print(arr[k]-1)

#
# ############
# https://devjin-blog.com/boj-1697-hideseek/