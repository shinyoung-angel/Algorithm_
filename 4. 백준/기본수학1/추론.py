import sys
input = sys.stdin.readline

n = int(input())
nums = list(int(input()) for _ in range(n))

flag = 1
for i in range(1, n-1):
    if nums[i] - nums[i-1] == nums[i+1] - nums[i]:
        pass
    else:
        flag = 0

if flag == 1:
    print(nums[-1] + (nums[1]-nums[0]))
else:
    print(int(nums[-1] * (nums[1]/nums[0])))

