



for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    result = 'a'

    if q1 < y2 or q2 < y1 or p1 < x2 or p2 < x1:
        result = 'd'

    elif p1 == x2:
        if y1 == q2 or q1 == y2:
            result = 'c'
        else:
            result = 'b'

    elif x1 == p2:
        if y1 == q2 or q1 == y2:
            result = 'c'
        else:
            result = 'b'

    elif q1 == y2:
        if p1 == x2 or p2 == x1:
            result = 'c'
        else:
            result = 'b'

    elif q2 == y1:
        if p1 == x2 or p2 == x1:
            result = 'c'
        else:
            result = 'b'

    print(result)


# ---------------

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    if p1 < x2 or q1 < y2 or p2 < x1 or q2 < y1:
        r = 'd'
    elif (p1==x2 and (y1==q2 or q1==y2)) or (x1==p2 and (y1==q2 or q1==y2)):
        r = 'c'
    elif (y1==q2 and x2<p1 and x1<p2) or (x2==p1 and y2<q1 and y1<q2) or (q1==y2 and x2<p1 and x1<p2) or (x1==p2 and y2<q1 and y1<q2):
        r = 'b'
    else:
        r = 'a'
    print(r)






