


for tc in range(1, int(input())+1):
    n = int(input())
    velocity = 0
    distance = 0

    for i in range(n):
        condition = list(map(int, input().split()))

        if condition[0] == 1:
            velocity = velocity + condition[1]

        elif condition[0] == 2:
            if condition[1] > velocity:
                pass

            else:
                velocity -= condition[1]

        elif condition[0] == 0:
            pass

        distance += velocity

    print('#{} {}'.format(tc, distance))