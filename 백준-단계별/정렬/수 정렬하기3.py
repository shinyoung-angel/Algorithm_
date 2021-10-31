import sys
input = sys.stdin.readline

n = int(input())
counting = [0] * 10001

for i in range(n):
    counting[int(input())] += 1

### 리스트에 있는 아이들 순서대로 출력
for i in range(len(counting)):
    if counting[i] != 0:
        for j in range(counting[i]):
            print(i)

