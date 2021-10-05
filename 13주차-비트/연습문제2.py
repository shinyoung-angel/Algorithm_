

## 16진수 --> 2진수 변환 함수
def binary(value):
    output = ''
    for j in range(3, -1, -1):
        output += '1' if value & ( 1 << j ) else '0'
    return output

hexa = 0x01D06079861D79F99F
word = ''
## 16진수 --> 2진수로 변환하고 word에다가 다 더해줌.
for i in range(len(str(hexa))-3, -1, -1):
    word += binary((hexa >> (i*4) ) & 0xff )

## 2진수 --> 10진수
length = 7
result = []

## 7비트씩 잘라주기
for i in range(0, len(word), length):
    result += [word[i:i+length]]
for i in result:
    print(int(i, 2), end= ' ')
