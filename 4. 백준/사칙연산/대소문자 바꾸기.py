
import sys
input = sys.stdin.readline

n = input()

for i in n:
    if i.isupper():
        print(i.lower(), end='')
    else:
        print(i.upper(), end='')