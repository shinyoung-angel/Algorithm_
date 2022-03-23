
import sys
input = sys.stdin.readline

a = int(input())
b = input().strip()
c = int(input())

if b == '*':
    print(a*c)
else:
    print(a+c)
