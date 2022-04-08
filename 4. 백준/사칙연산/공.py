
import sys
input = sys.stdin.readline

cup = [0, 1, 0, 0]

for _ in range(int(input())):
    a, b = map(int, input().split())
    cup[a], cup[b] = cup[b], cup[a]

print(cup.index(1))
