import sys
input = sys.stdin.readline


n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m = int(input())
compare = list(map(int, input().split()))

num_dic = {}

### 그냥 조건으로 if nums[i] 이렇게 하면 음수가 key값일 때 keyboard에러가 남
## 하쥐만 try, except는 된다,,,?????

for i in nums:
    try: num_dic[i] += 1
    except: num_dic[i] = 1

## 얘도 마찬가지로 조건으로 주면 안되고
## try, except로 하면 된다,,,,!!!!!
for j in compare:
    try:
        print(num_dic[j], end= ' ')
    except:
        print(0, end= ' ')


################

## 이분 탐색 힌트를 보고 이분탐색으로 풀었다
## 하쥐만 시간초과!!

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m = int(input())
compare = list(map(int, input().split()))

for tmp in compare:
    low = 0
    high = len(nums) - 1
    result = 0

    while low <= high:
        mid = (low+high) // 2

        if tmp == nums[mid]:
            result = nums[low:high+1].count(tmp)
            break
        elif nums[mid] > tmp:
            high = mid - 1
        else:
            low = mid + 1

    print(result, end=' ')


##################


### 헐,,, 카운팅 정렬,,!!!!!!
N=int(input())
nArr=list(map(int,sys.stdin.readline().split()))
M=int(input())
mArr=list(map(int,sys.stdin.readline().split()))

arr=[0]*20000001

for i in nArr:
    arr[i+10000000]+=1

for i in mArr:
    print(arr[i+10000000],end=" ")
