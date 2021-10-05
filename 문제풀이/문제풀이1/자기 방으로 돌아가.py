

def div(num):
    return (int(num) + 1) // 2

def maxmax(data):
    max_value = data[0]
    for i in range(len(data)):
        if max_value < data[i]:
            max_value = data[i]
    return max_value

for tc in range(1, int(input())+1):
    N = int(input())

    students = [list(map(div, input().split())) for _ in range(N)]

    road = [0] * 201

    for i in range(N):
        if students[i][0] > students[i][1]:
            students[i][0], students[i][1] = students[i][1], students[i][0]

        for j in range(students[i][0], students[i][1]+1):
            road[j] += 1


    print('#{} {}'.format(tc, maxmax(road)))
