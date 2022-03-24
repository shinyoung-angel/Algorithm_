
import sys
input = sys.stdin.readline

dot_dict = {'Q1':0, 'Q2':0, 'Q3':0, 'Q4':0, 'AXIS':0}

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 0 or b == 0:
        dot_dict['AXIS'] += 1
    elif a > 0 and b > 0:
        dot_dict['Q1'] += 1
    elif a < 0 and b > 0:
        dot_dict['Q2'] += 1
    elif a < 0 and b < 0:
        dot_dict['Q3'] += 1
    else:
        dot_dict['Q4'] += 1

for item, value in dot_dict.items():
    print('{}: {}'.format(item, value))


