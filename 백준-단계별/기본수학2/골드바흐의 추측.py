
import sys

# 먼저 소수 리스트를 구해놓기
prime = [1] * 10001

for i in range(2, int(10000 ** 0.5)+1):
    if prime[i] == 1:
        for j in range(2*i, 10001, i):
            prime[j] = 0


for _ in range(int(input())):
    n = int(sys.stdin.readline())

    # 소수의 차가 가장 작은 숫자들을 찾기 위한 가장 빠른 방법: 중가부터 찾기
    num = n // 2
    for i in range(num, 1, -1):
        if prime[i] and prime[n-i]:
            print(i, n-i)
            break


