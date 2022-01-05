

for tc in range(1, int(input())+1):
    n, k = map(int, input().split())

    gpa = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    total = []
    for i in range(n):
        test1, test2, hw = map(int, input().split())
        score = (test1*0.35) + (test2*0.45) + (hw*0.2)
        total.append(score)

    # 리스트를 그냥 복사하면 원본도 같이 바뀜 그래서 리스트 슬라이싱으로 복사하면 새로운 객체를 만들어서 ㄱㅊ 
    sort_total = total[:]

    for i in range(n-1, 0, -1):
        for j in range(i):
            if sort_total[j] < sort_total[j+1]:
                sort_total[j], sort_total[j+1] = sort_total[j+1], sort_total[j]

    # 원하는 번호의 학생 고르기
    who = total[k-1]
    # 성적을 10등분 하기 위함
    num = n // 10

    # 해당 학생이 등수로는 몇 등인가,,, 하는거쥐
    for i in range(n):
        if who == sort_total[i]:
            idx = i
    idxx = idx // num


    print('#{} {}'.format(tc, gpa[idxx]))