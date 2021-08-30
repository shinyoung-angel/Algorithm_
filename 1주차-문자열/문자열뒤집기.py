#1
a = list('삼성청년소프트웨어아카데미')

a_len = len(a)

for i in range(a_len//2):
    a[i], a[a_len - 1 - i] = a[a_len - 1 - i], a[i]
print(a)

#2
a.reverse()
print(a)


#3
print(a[::-1])

#4
for i in range(a_len-1, -1, -1):
    print(a[i], end='')
print()


# ------------------------------------------------------ #

def itoa():


