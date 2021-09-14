
# 어려웡..!!!!!

n = int(input())

# 사선이 몇 번째 줄인지 쳌
line = 0
# 사선이 제일 끝 숫자, 즉 다음 수열 ex, 1, 3, 6, 10
max_num = 0

# max_num이 n보다 더 커지면 break
while n > max_num:
    line += 1
    max_num += line

# 해당 자리가 끝의 숫자와 얼만큼 차이가 나는 지 알아야 분수를 구할 수 있음
gap = max_num - n
# 홀수 번째 줄일 때
if line % 2 == 0:
    # 분자/ 분모
    a = line - gap
    b = gap + 1
else:
    a = gap + 1
    b = line - gap

print('{}/{}'.format(a, b))