
# 받은 정보를 리스트에 저장하고 빈 문자열을 생성하여 여기다가 하나의 문자열로 만들어 줌
# 10개씩 끊어서 출력하는 방법은!!!!! 인덱스 슬라이싱!!! 10번씩 끊고 출력은 i부터 i+10까지


for tc in range(1, int(input() ) +1):
    n = int(input())

    arr = [list(input().split()) for _ in range(n)]
    new_list = ''


    for i in range(n):
        new_list += arr[i][0] *int(arr[i][1])


    print(f'#{tc}')
    for i in range(0, len(new_list), 10):
        print(new_list[i: i +10])