import sys
input = sys.stdin.read
result = [0]*26
s = input().replace("\n","").replace(" ","")
print(s)
for i in s:
    result[ord(i)-97] += 1

max_value = max(result)
ans = []
for i in range(26):
    if result[i] == max_value:
        ans.append(chr(i+97))

ans.sort()
print(*ans, sep="")
