


for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    work_list = [[] for _ in range(k+1)]

    ### 일의 리스트에 일을 하고 싶어하는 사람들의 번호 넣기
    for i in range(n):
        work = a[i]
        work_list[work].append(i+1)

    ### 일 --> 설득시간으로 변경
    for i in work_list:
        if len(i) >= 1:
            for j in i:
                work_list[i][j] = b[work_list[i][j]]


    print(work_list)
