import sys
input = sys.stdin.readline

vowel = ['a','e','i','o','u','A','E','I','O','U']

while True:
    word = list(input().strip().split())
    if word == ['#']: break
    ans = 0
    for tmp in word:
        for i in tmp:
            if i in vowel:
                ans += 1
    print(ans)
