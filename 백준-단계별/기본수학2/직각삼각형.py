


import sys

num = []
while True:

    n = list(map(int, sys.stdin.readline().split()))
    if n[0] == 0:
        break
    num.append(n)

for i in num:

    a, b, c = i[0]**2, i[1]**2, i[2]**2
    if a == b+c or b==a+c or c==a+b:
        print('right')
    else:
       print('wrong')

# ----------------------------

while True:
    numbers = list(map(int, input().split()))
    if numbers[0] == 0:
        break
    numbers.sort()

    if numbers[0]**2 + numbers[1]**2 == numbers[2]**2:
        print('right')
    else:
        print('wrong')