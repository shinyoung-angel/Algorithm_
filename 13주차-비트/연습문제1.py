

#  0000000111100000011000000111100110000110000111100111100111111001100111

## 0000000   1111000   0001100   0000111   1001100   0011000   0111100   1111001  1111100 1100111


def change(value):
    ans = 0
    if value == '0000000':
        return 0
    for j in range(6, -1, -1):
        ans += int(value[j]) * 2**(6-j)
    return ans

num = input()
word = []
length = 7
for i in range(0, len(num), length):
    word += [num[i:i+length]]

## 방법1
for i in word:
    print(change(i), end=' ')

## 방법2
for i in word:
    print(int(i, 2), end= ' ')