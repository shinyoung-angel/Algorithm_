import sys
input = sys.stdin.readline

t = int(input())
num_dict = {300:0, 60:0, 10:0}

for item in num_dict:
    if t >= item:
        cnt = t // item
        num_dict[item] = cnt
        t -= cnt * item

if t != 0:
    print(-1)
else:
    for item, value in num_dict.items():
        print(value, end=' ')
