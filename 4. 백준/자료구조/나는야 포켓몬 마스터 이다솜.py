
import sys
input = sys.stdin.readline

### '25', 'pikachu' 요 둘의 type을 어떻게 구분할 것인가~
#### 위의 방법을 고려했다면 시간초과가 났을 것

#### 딕셔너리를 두 개 만들기!



n, m = map(int, input().split())

num_key = {}
poke_key = {}

for i in range(n):
    tmp = input().strip()
    num_key[i+1] = tmp
    poke_key[tmp] = i+1

for i in range(m):
    tmp = input().strip()
    if tmp.isdigit():
        print(num_key[int(tmp)])
    else:
        print(poke_key[tmp])
