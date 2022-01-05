import sys
input = sys.stdin.readline

n = int(input())

fibo = [1, 1]

if n > 1:
    for i in range(2, n+1):
        fibo.append((fibo[i-1]+fibo[i-2])%15746)

print(fibo[n])