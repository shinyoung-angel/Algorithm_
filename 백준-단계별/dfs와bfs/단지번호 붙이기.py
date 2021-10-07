
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dfs(start, end):

    stack = [(start, end)]



n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited=[[] for _ in range(n)]

dfs(0, 0)