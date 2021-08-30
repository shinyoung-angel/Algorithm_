def inorder (n): # 시작 정점
    if n <= N:  # 유효한 정점이라면
        inorder(n*2) # 왼쪽 자식
        print(alphabet[n], end='') # 부모
        inorder(n*2+1) # 오른쪽 자식

for tc in range(1, 11):
    N = int(input())
    alphabet = [0] * (N+1) # 각 노드의 알파벳 정보를 입력해줄 것/ 시작 노드가 1이라 N+1만큼의 빈 리스트 필요

    for i in range(N):
        node = list(input().split())
        alphabet[i+1] = node[1] # 알파벳을 쏙쏙 넣어 줌

    print('#{}'.format(tc), end = ' ')
    inorder(1) # 시좍
    print()


