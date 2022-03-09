import sys
input = sys.stdin.readline


n, m = map(int, input().split())
password_dict = {}

for _ in range(n):
    a, b = input().strip().split()
    password_dict[a] = b
for _ in range(m):
    tmp = input().strip()
    print(password_dict[tmp])