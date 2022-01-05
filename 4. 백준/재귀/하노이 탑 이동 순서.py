
def hanoi(no, start, end):

    if no > 1:
        hanoi(no-1, start, 6-start-end)

    print('{} {}'.format(start, end))

    if no > 1:
        hanoi(no-1, 6-start-end, end)


n = int(input())
print(2**n - 1)
hanoi(n, 1, 3)