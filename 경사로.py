import copy, sys
input = sys.stdin.readline


n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

def check(line):

    tmp = 0
    flag = 1

    while tmp != len(line):
        tmp += 1
        try:
            extract = abs(line[tmp] - line[tmp-1])
            real_extract = line[tmp] - line[tmp-1]
        except:
            break

        if extract == 0:
            continue

        elif extract == 1:
            try:
                for i in range(l):
                    if line[tmp] == line[tmp+i]:
                        tmp += l - 1
                    else:
                        flag = 0
                        break
                line[tmp] -= real_extract

            except:
                flag = 0
                break
        else:
            flag = 0
            break

    return flag

for i in range(n):
    n_arr = copy.deepcopy(arr)
    cnt += check(n_arr[i]) + check(n_arr[:][i])

print(cnt)



