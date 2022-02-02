
a, b = map(int, input().split())

print(a*(b-1)+1)


#####

### 세 수
#### 브론즈3
a = list(map(int, input().split()))
a.sort()
print(a[-2])