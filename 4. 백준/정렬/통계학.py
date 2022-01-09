import sys
input = sys.stdin.readline

n = int(input())

num_dic = {}
arr= []

for _ in range(n):
    tmp = int(input())
    try: num_dic[tmp] += 1
    except: num_dic[tmp] = 1
    arr.append(tmp)

arr.sort()

print(int(round(sum(arr)/n)))

print(arr[n//2])

values = num_dic.values()
max_value = max(values)
result = []
for key, value in num_dic.items():
    if value == max_value:
        result.append(key)

if len(result) == 1:
    print(*result)
else:
    result.sort()
    print(result[1])


print(max(arr)-min(arr))