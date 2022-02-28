import sys
input = sys.stdin.readline

## count하는 것이 아니라 숫자의 크기 순위를 구하는 문제!!!
## 물론 count해도 되지만 시간초과 남!!
n = int(input())
arr = list(map(int, input().split()))
arr2 = list(sorted(set(arr)))

###########
arr_dict = { arr2[i]:i for i in range(len(arr2))}
for i in arr:
    print(arr_dict[i], end=' ')





# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = list(map(int, input().split()))
# arr_dict = {i:0 for i in arr}
#
# for i in arr:
#     arr_dict[i] += 1
#
# for i in arr:
#     ans = 0
#     for key, value in arr_dict.items():
#         if i > key:
#             ans += 1
#     print(ans, end= ' ')
