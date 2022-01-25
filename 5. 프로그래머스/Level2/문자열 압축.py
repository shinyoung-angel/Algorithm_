

def check(word,num):

    cnt = 0
    repeat = 1
    for i in range(0, len(word)-num, num):
        last = i+num
        tmp = word[i:i+num]
        if tmp == word[i+num:i+2*num]:
            repeat += 1
        else:
            if repeat == 1:
                cnt += num
            else:
                cnt += len(str(repeat)) + num
                repeat = 1

    if repeat == 1:
        cnt += len(word[last:len(word)])
    else:
        cnt += len(str(repeat)) + num

    return cnt

s = input()
min_value = 1001

## 문자열의 길이가 5라면, 1,2,3,4,5개 단위로 확인할 것
for i in range(1,len(s)):
    min_value = min(min_value, check(s, i))

## 문자열 길이가 1이라면 1을 반환
if min_value == 1001:
    print(1)
else:
    print(min_value)

