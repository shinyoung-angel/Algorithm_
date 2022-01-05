

## 한 방에 최대 수까지 만들어 놓기 ####

max_range = 123456*2
prime = [1] * (max_range+1)

for i in range(2, int(max_range ** 0.5)+1):
    if prime[i] == 1:
        for j in range(2*i, max_range+1, i):
            prime[j] = 0


num = []
while True:

    n = int(input())
    if n == 0:
        break
    num.append(n)

for i in num:

    cnt = 0
    for j in range(i+1, 2*i + 1):
        if prime[j]:
            cnt += 1

    print(cnt)



# ------정답~~~~~~~~~~~~~~~~~~~~~~~~~~

num = []
while True:
    n = int(input())
    if n == 0:
        break
    num.append(n)


for i in num:

    prime = [1] * ((2*i)+1)
    for j in range(2, int(2*i**0.5)+1):
        if prime[j] == 1:
            for k in range(2*j, ((2*i)+1), j):
                prime[k] = 0

    cnt = 0
    for j in range(i+1, (2*i)+1):
        if j >1 and prime[j] == 1:
            cnt += 1

    print(cnt)

#-------------
