

n = int(input())
vowels = ['A','E','I','O','U','a','e','o','i','u']
for _ in range(n):
    tmp = list(input().split())
    con = 0
    vo = 0
    for i in tmp:
        for j in i:
            if j in vowels:
                vo += 1
            else:
                con += 1
    print(con, vo)