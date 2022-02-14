import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

num_dict = {i:0 for i in arr}

for i in card:
    try:
        num_dict[i] += 1
    except: pass


for key, value in num_dict.items():
    print(value, end=' ')