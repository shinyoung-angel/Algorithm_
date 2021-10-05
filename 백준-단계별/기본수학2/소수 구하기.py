

# ------------------------ 증답 시간 엄청 오래 걸림


m, n = map(int, input().split())

for i in range(m, n+1):
    cnt = 0

    if i == 1:
        continue

    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            cnt += 1
            break

    if cnt == 0:
        print(i)
# -----------------------------증답~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def check(num):

    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

m, n = map(int, input().split())

for i in range(m, n+1):
    if check(i):
        print(i)

# ----------
### 에라토스테네스의 체


m, n = map(int, input().split())

## 체 준비
prime = [1] * (n+1)

for i in range(2, int(n**0.5)+1):
    if prime[i] == 1:
        for j in range(2*i, n+1, i):
            prime[j] = 0

for i in range(m, n+1):
    if i >1 and prime[i] == 1:
        print(i)


