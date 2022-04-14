
min_prob = ''
min_num = 100
for _ in range(int(input())):
    problem, level = input().split()
    if int(level) < min_num:
        min_num = int(level)
        min_prob = problem

print(min_prob)