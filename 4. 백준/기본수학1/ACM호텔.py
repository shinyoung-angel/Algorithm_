
# 내가 푼 방법은 시간이 매우 걸리며 bruteforce네
for _ in range(int(input())):
    h, w, n = map(int, input().split())
    arr = [[0]*(w+1) for _ in range(h)]


## 인덱스 낮은 열의 아이들부터 하나하나 첵 하고 n번째 췍한 아이의 인덱스를 가져와서 방 번호로 만들기
    cnt = 0
    for i in range(1, w+1):
        for j in range(h):
            arr[j][i] = 1
            cnt += 1
            if cnt == n:
                floor = j + 1
                room = i
                break

    if room >= 10:
        print(str(floor)+str(room))

    else:
        print((str(floor)+'0'+str(room)))

# --------------


# 층 수는 손님의 번호에서 최대 층수인 h를 나눈 나머지
# 방 번호는 손님의 번호에서 층 수를 몫에다가 1을 더하기

# 하지만 층수가 h의 배수인 경우를 고려해줘야함. 그렇담 층수는 꼭대기층이며 방 번호는 하나 빼야 함.
for _ in range(int(input())):
    h, w, n = map(int, input().split())

    floor = n % h
    room = n // h + 1

    if floor == 0:
        floor = h
        room -= 1

    print(floor*100+room)


