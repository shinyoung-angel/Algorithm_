
## 조합의 모든 경우의 수를 고려했음
## 조합의 수가 3개면 됐기 때문에 가능했음. 숫자가 크다면 런타임 에러날 듯

n, m = map(int, input().split())
cards = list(map(int, input().split()))

## 가능한 모든 경우의 수를 set에 추가해주기
ans_list = set()
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            num_sum = cards[i] + cards[j] + cards[k]
            ans_list.add(num_sum)

## 그중 m 이하이면서 젤 큰 수를 고르기,, max함수를 썼어도 될 일이군,,,
answer = 0
for i in ans_list:
    if i <= m:
        if i >= answer:
            answer = i

print(answer)





