


max_player = 0
max_score = 0

for i in range(1, 6):
    tmp = sum(list(map(int, input().split())))

    if tmp > max_score:
        max_player = i
        max_score = tmp

print(max_player, max_score)