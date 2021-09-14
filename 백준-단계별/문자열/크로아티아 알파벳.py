

a = input()
ans = 0
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

#  8종류의 알파벳이 a에 몇 개 있나 확인하고 ans에다 넣어 줌.
# 그리고 췌 한 알파벳은 0으로 바꿔줌. 그리고 다음 알파벳 췤
for i in alpha:
    ans += a.count(i)
    a = a.replace(i, '0')

# 다 췤하고 알파벳이 아니라 0으로 바뀌지 못했던 아이들까지 갯수를 세어 줌.
for i in a:
    if i != '0':
        ans += 1
print(ans)
