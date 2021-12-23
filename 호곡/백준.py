


n = int(input())
deque = []
arr = [input() for _ in range(n)]

for tmp in arr:

    if tmp[0:10] == 'push_front':
        deque.insert(0, int(tmp[11:]))

    elif tmp[0:9] == 'push_back':
        deque.append(int(tmp[10:]))

    elif tmp == 'pop_front':
        if not deque:
            print(-1)
        else:
            print(deque.pop(0))

    elif tmp == 'pop_back':
        if not deque:
            print(-1)
        else:
            print(deque.pop())

    elif tmp == 'size':
        print(len(deque))

    elif tmp == 'empty':
        if not deque:
            print(1)
        else:
            print(0)

    elif tmp == 'front':
        if not deque:
            print(-1)
        else:
            print(deque[0])

    elif tmp == 'back':
        if not deque:
            print(-1)
        else:
            print(deque[-1])



