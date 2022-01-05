import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    tmp = list(input().split())
    tmp.append(i)
    arr.append(tmp)

##### 여기서 int(x[0])으로 줘야 함!!!! 문자열로 들어왔기 때문에 숫자로 바꿔주기~~
arr.sort(key=lambda x:(int(x[0]), x[2]))

for tmp in arr:
    print(*tmp[:2])