



a, b, c = map(int, input().split())

# 밑 빠진 독에 물 붓기
if b >= c:
    print(-1)

# A // (c-b) 하고 1을 더해줘야 하는 이유는!! 금액이 0을 넘어야 손익분기점이니까!
else:
    print(int(a//(c-b)+1))