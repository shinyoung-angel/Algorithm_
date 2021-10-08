


for tc in range(1, int(input())+1):
    a = list(input())
    b = list(input())

    binary_list = []
    for i in range(len(a)):                     # 2진수를 한자리씩만 바꿔서 리스트에 넣어줌.
        if a[i] == '1':
            a[i] = '0'
            binary_list.append(''.join(a))
            a[i] = '1'
        else:
            a[i] = '1'
            binary_list.append(''.join(a))
            a[i] = '0'

    tri_list = []
    for i in range(len(b)):
        if b[i] == '2':
            b[i] = '0'
            tri_list.append(''.join(b))
            b[i] = '1'
            tri_list.append(''.join(b))
            b[i] = '2'
        elif b[i] == '0':
            b[i] = '1'
            tri_list.append(''.join(b))
            b[i] = '2'
            tri_list.append(''.join(b))
            b[i] = '0'
        else:
            b[i] = '0'
            tri_list.append(''.join(b))
            b[i] = '2'
            tri_list.append(''.join(b))
            b[i] = '1'

    ans = 0
    for i in binary_list:
        a = int(i, 2)
        for j in tri_list:
            b = int(j, 3)
            if a == b:
                ans = a
                break
        if ans:
            break

    print('#{} {}'.format(tc, ans))


# ----------------------------------------

# 10진수로 바꾸는 함수
def change_to_dec(num, notation):           #입력받은 문자열, 몇진수인가// 문자열로 받아서 뒤집어서 쓰겠다
    tmp = 0                                 # 임시로 쓸 값

    for n, val in enumerate(list(map(int, num))[::-1]):
        tmp += val * (notation**n)
    return tmp


# def change_to_dec2(num, notation):
#     tmp = 0
#     n = len(num) - 1
#
#     for i in map(int, num):
#         tmp += i * (notation**n)
#         n -= 1
#     return tmp


def check(num, notation):
    change_num = change_to_dec(num, notation)
    # change_num = int(num, notation)

    for n, val in enumerate(list(map(int, num))[::-1]):
        for j in range(notation):
            if val == j: continue
            tmp = change_num - i *(notation**n) + j * (notation**n)

            if tmp not in binary:
                binary.append(tmp)

            else:
                return tmp



# def check2():
#     bi_num = 0
#     for x in bi:
#         bi_num = bi_num*2 + int(x)
#
#     for i in range(len(bi)):
#         binary.append(bi_num ^ (1<<i))
#
#     for i in range(len(tr)):
#         num1 = 0
#         num2 = 0
#
#         for j in range(len(tr)):
#             if i != j:
#                 num1 = num1 * 3 + int(tr[j])
#                 num2= num2 * 3 + int(tr[j])
#             else:
#                 num1 = num1 * 3 + (int(tr[j])+1)%3
#                 num2 = num2 * 3 + (int(tr[j])+2)%3
#
#         if num1 in binary:
#             return num1
#         if num2 in binary:
#             return  num2




for tc in range(1, int(input())+1):
    bi = input()
    tr = input()

    binary = []
    check(bi, 2)

    # check2()

    print('#{} {}'.format(tc, check(tr, 3)))






