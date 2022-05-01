

# 이거 왜 틀림?????
n = int(input())

ans = 0

for i in range(n):
    tmp = int(input())
    if tmp % 2 == 1:
        ans += tmp
        print(ans)

# 이건 마즘!!!! 왜??
for _ in range(int(input())):
    N = int(input())
    print(sum([n for n in range(1, N+1) if n%2]))