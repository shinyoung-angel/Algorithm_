import sys
input = sys.stdin.readline

def queen(cnt):
    global result

    if cnt == n:
        result += 1
        return



n = int(input())
visited = [0]* n
result = 0