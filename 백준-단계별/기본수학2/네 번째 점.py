


#### 딕셔너리 사용~~~~~

point = [list(map(int, input().split())) for _ in range(3)]

left = {}
right = {}

for i in range(3):

    #왼쪽
    if left.get(point[i][0]):
        left[point[i][0]] += 1
    else:
        left[point[i][0]] = 1

    #오른쪽
    if right.get(point[i][1]):
        right[point[i][1]] += 1
    else:
        right[point[i][1]] = 1

for key, value in left.items():
    if value == 1:
        print(key, end=' ')
for key, value in right.items():
    if value == 1:
        print(key)




#### 리스트 사용~~~~~

x_list = []
y_list = []

for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for i in range(3):
    if x_list.count(x_list[i]) == 1:
        x = x_list[i]
    if y_list.count(y_list[i]) == 1:
        y = y_list[i]
print(x, y)

