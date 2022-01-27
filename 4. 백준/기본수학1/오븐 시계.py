import sys
input = sys.stdin.readline


a, b = map(int, input().split())
time = int(input())

tmp = time + b

if tmp >= 60:
    a += tmp // 60
    tmp -= tmp // 60 * 60

print(a%24, tmp)