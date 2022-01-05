
for i in range(1, int(input())+1):
    N = input()
    card = list(map(int, input()))
    counting = [0] * 10
    cnt = 0
    max_value = 0

    for k in card:
        counting[k] += 1


    for j in range(len(counting)-1, -1, -1):
        if counting[j] > max_value:
            max_value = counting[j]
            cnt = j


    print('#{} {} {}'.format(i, cnt, max_value))











    # for j in range(1, 10):
    #     counting[j] += counting[j-1]
    #
    # for h in range(len(card)-1, -1, -1):
    #     new[counting[card[h]]-1] = card[h]
    #     counting[card[h]] -= 1



