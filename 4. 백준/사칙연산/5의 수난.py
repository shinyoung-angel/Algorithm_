
import sys
input = sys.stdin.readline

word = input()

ans = 0

for i in range(5):
    tmp = int(word[i])
    ans += tmp ** 5

print(ans)