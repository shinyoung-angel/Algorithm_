import sys
input = sys.stdin.readline

n = int(input())
word = input()
ans = 0

for i in range(n):
    tmp = word[i]
    ans += (ord(tmp)-96) * 31**i

## 그냥 ans는 50점이다!
# print(ans)

## mod M 이라는 조건이 있었다!
print(ans % 1234567891)