

## 이거 runtime error 뜸
a, b, v = map(int, input().split())

cnt = 1
tree = 0

while True:

    tree += a

    if tree >= v:
        break
    tree -= b
    cnt += 1

print(cnt)

# ----------- 계산으로 푸는 방법

a, b, v = map(int, input().split())

# 낮에 도달한 경우도 고려해줘야 함 따라서 나무 길이 에서 밤 길이를 한 번 빼고 나눠줄 것
if (v-b) % (a-b) == 0:
    print((v-b)//(a-b))
else:
    print((v-b)//(a-b)+1)


a, b, v = map(int, input().split())
# 낮에 도달한 경우도 고려해줘야 함 따라서 나무 길이 에서 밤 길이를 한 번 빼고 나눠줄 것
tree = v-b
climb = a-b
if tree % climb == 0:
    print(tree//climb)
else:
    print(tree//climb+1)
