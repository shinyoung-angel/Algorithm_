import sys
input = sys.stdin.readline

n = int(input())
word_set = []
for _ in range(n):
    word = input().strip()
    word_set.append((word, len(word)))

word_set = list(set(word_set))
word_set.sort(key=lambda x:(x[1], x[0]))
for i in range(len(word_set)):
    print(word_set[i][0])

