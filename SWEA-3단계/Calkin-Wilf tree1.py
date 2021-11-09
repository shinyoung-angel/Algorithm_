

for tc in range(1, int(input())+1):
    direction = input()

    tree = [[1, 1]]

    for i in range(len(direction)):
        left = tree[i][0]
        right = tree[i][1]
        if direction[i] == 'L':
            tree.append([left, left+right])
        else:
            tree.append([left+right, right])


    print('#{} {} {}'.format(tc, tree[-1][0], tree[-1][1]))

