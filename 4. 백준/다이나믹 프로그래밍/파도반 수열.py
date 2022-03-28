

import sys
input = sys.stdin.readline

arr = [1, 1, 1, 2, 2]

for i in range(5, 101):
    arr.append(arr[i-1]+arr[i-5])

for _ in range(int(input())):
    num = int(input())
    print(arr[num-1])
