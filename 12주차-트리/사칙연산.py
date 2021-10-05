
def postorder(n):

    if n >= node: return

    if tree[n][1]:
       postorder(tree[n][1])
    if tree[n][2]:
       postorder(tree[n][2])


    if tree[n][0] == '+':
        tree[n][0] = tree[tree[n][1]][0] + tree[tree[n][2]][0]
    elif tree[n][0] == '-':
        tree[n][0] = tree[tree[n][1]][0] - tree[tree[n][2]][0]
    elif tree[n][0] == '*':
        tree[n][0] = tree[tree[n][1]][0] * tree[tree[n][2]][0]
    elif tree[n][0] == '/':
        tree[n][0] = tree[tree[n][1]][0] / tree[tree[n][2]][0]


for tc in range(1, 11):
    node = int(input())
    tree = [[0, 0, 0] for _ in range(node+1)]

    for n in range(node):
        node_info = list(input().split())
        if node_info[1].isdigit():
            tree[int(node_info[0])][0] = int(node_info[1])
        else:
            tree[int(node_info[0])][0] = node_info[1]
            tree[int(node_info[0])][1] = int(node_info[2])
            tree[int(node_info[0])][2] = int(node_info[3])

    postorder(1)
    print('#{} {}'.format(tc, int(tree[1][0])))




