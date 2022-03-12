money = 1999
costs = [2, 11, 20, 100, 200, 600]


def solution(money, costs):
    cost_dict = {1: costs[0], 5: costs[1], 10: costs[2], 50: costs[3], 100: costs[4], 500: costs[5]}
    cost_per_dict = {1: costs[0] / 1, 5: costs[1] / 5, 10: costs[2] / 10, 50: costs[3] / 50, 100: costs[4] / 100,
                     500: costs[5] / 500}
    cpd = sorted(cost_per_dict.items(), key=lambda x: x[1])
    answer = 0
    money_order = 0

    while money > 0 and money_order < 6:

        now_money = cpd[money_order][0]
        if now_money <= money:
            cnt = money // now_money
            answer += cnt * cost_dict[now_money]
            money -= cnt * now_money

        money_order += 1

    return answer

print(solution(money, costs))
