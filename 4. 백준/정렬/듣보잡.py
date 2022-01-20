import sys
input = sys.stdin.readline


## 시간초과
n, m = map(int, input().split())
cnt = 0
result = []
no_listen = list(input() for _ in range(n))

for _ in range(m):
    tmp = input()
    if tmp in no_listen:
        cnt += 1
        result.append(tmp)

result.sort()
print(cnt)

for i in result:
    print(i)


### 이거 집합으로 풀어야 해~~~~~

n, m = map(int, input().split())

no_listen = list(input() for _ in range(n))
no_hear = list(input() for _ in range(m))

########## set & set로 교집합을 구할 수 있다~!!!!!!!!
result = list(set(no_listen) & set(no_hear))

print(len(result))
result.sort()
for i in result:
    print(i, end= '')