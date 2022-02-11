



arr = list(map(int, input().split()))
arr_dict = {i:0 for i in arr}       ## 미리 딕셔너리 생성 후 카운트 해줌

for i in arr:
    tmp = arr.count(i)
    arr_dict[i] = tmp

max_cnt = 1
max_num = 0
for key, value in arr_dict.items():
    if value > max_cnt:
         max_cnt = value
         max_num = key

if max_cnt == 3:
    print(10000+(max_num*1000))
elif max_cnt == 2:
    print(1000+(max_num*100))
else:
    print(max(arr)*100)



