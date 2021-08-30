# 버블 정렬
def bubble(a):
    for i in range(len(a)-1, 0, -1):
        for k in range(0, i):
            if a[k] > a[k+1]:
                a[k], a[k+1] = a[k+1], a[k]

    return a
a = [55, 7, 78, 12, 42]
a.sort()
print(bubble(a))



