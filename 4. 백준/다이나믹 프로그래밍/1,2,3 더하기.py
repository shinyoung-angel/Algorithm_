import sys
input = sys.stdin.readline

def change(number):

    if number == 1: return 1
    elif number == 2: return 2
    elif number == 3: return 4
    else:
        return change(number-1) + change(number-2) + change(number-3)

for _ in range(int(input())):
    num = int(input())
    print(change(num))

