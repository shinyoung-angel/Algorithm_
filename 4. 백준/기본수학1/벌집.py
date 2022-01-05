
# 거꾸로 숫자를 빼주기

n = int(input())

cnt = 1

while n > 1:

    n -= 6 *cnt
    cnt += 1
print(cnt)

# ---------------

# 차근차근 수열

n = int(input())
cnt = 1
total = 1

while True:

    if n <= total:
        break

    total += 6 * cnt
    cnt += 1

print(cnt)
