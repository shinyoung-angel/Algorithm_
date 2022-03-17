w = 4
h = 4

def solution(w,h):
    total = w * h
    answer = total
    small = min(w, h)
    big = max(w, h)
    mod = big // small

    if w == h:
        answer -= w
    elif w == 1 or h == 1:
        answer = 0
    elif mod < 2:
        answer -= 2* small
    else:
        answer -= 3*small

    return answer

print(solution(w, h))