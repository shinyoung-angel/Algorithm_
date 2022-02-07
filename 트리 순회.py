import sys
input = sys.stdin.readline


n = int(input())
tree = {}

for _ in range(n):
    tmp = list(input().split())
    tree[tmp[0]] = tmp

def pre(x):

    print(tree[x][0], end='')
    if tree[x][1] != '.': pre(tree[x][1])
    if tree[x][2] != '.': pre(tree[x][2])


def in_(x):

    if tree[x][1] != '.': in_(tree[x][1])
    print(tree[x][0], end='')
    if tree[x][2] != '.': in_(tree[x][2])

def post(x):

    if tree[x][1] != '.': post(tree[x][1])
    if tree[x][2] != '.': post(tree[x][2])
    print(tree[x][0], end='')

pre('A')
print()
in_('A')
print()
post('A')

7
A B C
B D .
C E F
E . .
F . G
D . .
G . .