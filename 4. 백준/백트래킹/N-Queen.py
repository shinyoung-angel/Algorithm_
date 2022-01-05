import sys
input = sys.stdin.readline



############################ 모르겠다 #####################################
def check(x):
    for i in range(x):
        if visited[x] == visited[i] or abs(visited[i]-visited[x]) == x-i:
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
        return

    for i in range(n):
        visited[x] = i
        if check(x):
            dfs(x+1)

n = int(input())
visited = [0]* n
result = 0

dfs(0)
print(result)