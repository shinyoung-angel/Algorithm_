import sys
input = sys.stdin.readline

word = list(input().strip())

result = 1
for i in range(len(word)//2):
    tmp = word[i]
    tmp_2 = word[-i-1]
    if tmp != tmp_2:
        result = 0
        break

print(result)