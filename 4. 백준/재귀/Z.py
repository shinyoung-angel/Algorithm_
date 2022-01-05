import sys
input = sys.stdin.readline

### 왕,,,, 분할정복 생각도 못했다,,,!!
### 재귀로 푸는 방법은 아직 잘 모르겠다
## 복습 ㄱ ㄱ

n, r, c = map(int,input().split())
ans = 0
while n!= 0:

    n -= 1

    ## 1사분면일 때
    if r < 2**n and c < 2**n:
        pass

    ## 2사분면
    elif r < 2**n and c >= 2**n:
        ans += 2**n * 2**n
        c -= 2**n

    ## 3사분면
    elif r >= 2**n and c < 2**n:
        ans += 2**n * 2**n * 2
        r -= 2**n

    ## 4사분면
    else:
        ans += 2**n * 2**n * 3
        r -= 2**n
        c -= 2**n

print(ans)

##########

def solve(x, y, n):
    if n == 1:
        return 2 * x + y
    else:
        if x < 2 ** (n - 1):
            if y < 2 ** (n - 1):
                return solve(x, y, n - 1)
            else:
                return solve(x, y - 2 ** (n - 1), n-1) + 2 ** (2 * n - 2)
        else:
            if y < 2 ** (n - 1):
                return solve(x-2**(n-1), y, n-1)+ 2**(2*n-1)
            else:
                return solve(x-2**(n-1), y-2**(n-1), n-1) +2**(2*n-2)*3
n,x,y = map(int, input().split())
print(solve(x,y,n))


#####

N, r, c = map(int, input().split())

def func(N, r, c):
    if N == 0:
        return 0
    else:
        return 4 * func(N-1, r//2, c//2) + (r % 2) * 2 + (c % 2) * 1

print(func(N, r, c))