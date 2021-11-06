import sys
input = sys.stdin.readline

zero = [1, 0, 1]            ## 얘네들도 결국은 피보나치 수열임!!
one = [0, 1, 1]

def fibo(x):

    length = len(zero)
    if length <= x:
        for i in range(length, x+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append((one[i-1]+one[i-2]))
    print(zero[x], one[x])

for tc in range(int(input())):
    n = int(input())
    fibo(n)


#######################################
## 미리 리스트에 담아두기


import sys
input = sys.stdin.readline
fibo = [0, 1, 1]

for i in range(3,41):
    fibo.append(fibo[i-1]+fibo[i-2])

for tc in range(int(input())):
    n = int(input())

    if n == 0:
        print(1, 0)
    else:
        print(fibo[n-1], fibo[n])