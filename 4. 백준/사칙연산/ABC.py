

arr = list(map(int, input().split()))
arr.sort()

word = input()

for i in range(3):
    if word[i] == 'A': print(arr[0], end=' ')
    elif word[i] == 'B': print(arr[1], end=' ')
    else: print(arr[2], end=' ')