

# a = 3.14159265
#
# print('%.4f'%a)
# print(f'{a: .4f}')
#
#
# import sys
# sys,stdin = open('---.txt', 'r')

# print(ord('x'))


# ```
# 6 8
# 0 1 0 2 0 5 0 6 4 3 5 3 5 4 6 4
# ```

node, edge = map(int, input().split())
arr = list(map(int, input().split()))
matrix = [[0]*(node+1) for _ in range(node+1)]

for i in range(edge):
    st = arr[i*2]
    ed = arr[i*2+1]
    matrix[st][ed] = 1
    matrix[ed][st] = 1

adj_list = [[] for _ in range(node+1)]

for i in range(edge):
    st = arr[i * 2]
    ed = arr[i * 2 + 1]
    adj_list[st].append(ed)
    adj_list[ed].append(st)

print(adj_list)