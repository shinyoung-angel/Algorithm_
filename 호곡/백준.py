# import sys
# input = sys.stdin.readline


n = int(input())
arr = [input() for _ in range(n)]
queue = []
for tmp in arr:

    if tmp[:4] == 'push':
        queue.append(int(tmp[5:]))

    elif tmp == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))

    elif tmp == 'size':
        print(len(queue))

    elif tmp == 'empty':
        if not queue:
            print(1)
        else:
            print(0)

    elif tmp == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])

    elif tmp == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])