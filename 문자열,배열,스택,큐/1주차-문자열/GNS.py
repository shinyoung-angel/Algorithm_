#GNS 숫자를 영어에다가 할당(?)



num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, int(input())+1):
    N, length = map(str, input().split())
    length = int(length)
    TC = list(map(str, input().split()))
    ans = []

    for i in range(len(num)):
        for k in TC:
            if num[i] == k:
                ans.append(k)
    print(N)
    print(*ans)

