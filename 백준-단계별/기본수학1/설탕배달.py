
# 꽤나 어렵구먼
# 5키로 짜리가 많으면 좋다. 하지만 그렇게 하기 위해서는 5의 배수를 만들어 줘야 함.
# 설탕에서 3키로씩 빼서 5의 배수가 되는 지 확인하고 cnt추가
# 만약 3키로와 5키로로 계산할 수 없다면 설탕이 음수가 되고 -1을 출력할 것

sugar = int(input())
cnt = 0

while sugar >= 0:

    if sugar % 5 == 0:
        cnt += sugar // 5
        break

    sugar -= 3
    cnt += 1

else:
    cnt = -1

print(cnt)