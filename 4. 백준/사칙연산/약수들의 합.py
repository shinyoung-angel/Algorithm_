import sys
input = sys.stdin.readline


while True:
    num = int(input())
    if num == -1: break

    divided = []

    for i in range(1, num):
        if num % i == 0:
            divided.append(i)

    if num == sum(divided):
        result = str(num) + ' = '
        for j in range(len(divided)):
            tmp = divided[j]
            if tmp == divided[-1]:
                result += str(tmp)
            else:
                result += str(tmp) + ' + '
        print(result)
    else:
        print('{} is NOT perfect.'.format(num))